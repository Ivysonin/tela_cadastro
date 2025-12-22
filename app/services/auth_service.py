from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash ,check_password_hash
from app.models.user_model import User
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema
from app import db


class AuthService:

    @staticmethod
    def register(data):
        """
        Registra um novo usuário

        data = {
            "nome": "",
            "email": "",
            "senha": ""
        }
        """
        schema = UserSchema()

        try:
            validated = schema.load(data)
        except ValidationError as err:
            return {"errors": err.messages}, 400
        

        nome = data["nome"].strip()
        email = data["email"].lower()

        if User.query.filter_by(email=email).first():
            return {"error": "E-mail já cadastrado"}, 409

        user = User(
            nome=nome,
            email=email,
            senha_hash=generate_password_hash(data["senha"])
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "Usuário registrado com sucesso"}, 201

    @staticmethod
    def login(email, senha):
        """
        data = {
            "email": "",
            "senha": ""
        }
        """

        user = User.query.filter_by(email=email.lower()).first()

        if not user:
            return {"error": "Usuário não encontrado"}, 404

        if not check_password_hash(user.senha_hash, senha):
            return {"error": "Senha incorreta"}, 401

        login_user(user)
        return {"message": "Login realizado com sucesso"}, 200

    @staticmethod
    def logout():
        logout_user()
        return {"message": "Logout realizado com sucesso"}, 204