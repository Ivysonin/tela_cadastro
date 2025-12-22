from werkzeug.security import generate_password_hash, check_password_hash
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.user_model import User
from app import db


class UserService:

    @staticmethod
    def update_user(user, data):
        """
        Atualiza um usuário

        data = {
            "nome": "",
            "email": "",
            "senha_atual": "",
            "nova_senha": "",
            "confirmar_senha": ""
        }

        AVISO: Não precisa passar todos os campos, apenas aqueles que vão ser atualizados.
        """

        schema = UserSchema(partial=True)

        # Remove campos que não pertencem ao schema antes de validar
        extra_fields = ["senha_atual", "nova_senha", "confirmar_senha"]
        data_for_schema = {k: v for k, v in data.items() if k not in extra_fields}

        try:
            validated = schema.load(data_for_schema)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        if "email" in validated:
            email = validated["email"].lower()
            if User.query.filter(User.email == email, User.id != user.id).first():
                return {"error": "E-mail já cadastrado"}, 409
            user.email = email

        senha_atual = data.get("senha_atual")
        nova_senha = data.get("nova_senha")
        confirmar_senha = data.get("confirmar_senha")
        
        if senha_atual and nova_senha and confirmar_senha:
            # Verifica se a senha atual está correta
            if not check_password_hash(user.senha_hash, senha_atual):
                return {"error": "Senha atual incorreta"}, 400

            # Verifica tamanho mínimo
            if len(nova_senha) < 6:
                return {"error": "A nova senha deve ter no mínimo 6 caracteres"}, 400

            # Verifica se nova senha e confirmação coincidem
            if nova_senha != confirmar_senha:
                return {"error": "As senhas não coincidem"}, 400

            user.senha_hash = generate_password_hash(nova_senha)

        db.session.commit()
        return {"message": "Usuário atualizado com sucesso"}, 200