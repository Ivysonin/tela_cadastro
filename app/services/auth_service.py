from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash ,check_password_hash
from app.models.user_model import User
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema
from app.core.exceptions import NotFoundException, UnauthorizedException, ValidationException
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
            raise ValidationException(errors=err.messages)

        nome = data["nome"].strip()
        email = data["email"].lower()

        if User.query.filter_by(email=email).first():
            raise ValidationException(message="E-mail já cadastrado", errors={'email':"Já existe um usuário com este e-mail"})

        user = User(
            nome=nome,
            email=email,
            senha_hash=generate_password_hash(data["senha"])
        )

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def login(data):
        """
        data = {
            "email": "",
            "senha": ""
        }
        """
        email = data.get("email")
        senha = data.get("senha")

        user = User.query.filter_by(email=email.lower()).first()

        if not user:
            raise NotFoundException("Usuário não encontrado")

        if not check_password_hash(user.senha_hash, senha):
            raise UnauthorizedException("Senha incorreta")

        login_user(user, remember=True)
        return user

    @staticmethod
    def logout():
        logout_user()