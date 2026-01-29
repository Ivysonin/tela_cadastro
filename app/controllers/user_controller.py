from flask import Blueprint, request
from flask_login import login_required, current_user
from app.schemas.user_schema import UserSchema
from app.services.user_service import UserService
from app.core.response import success


user_bp = Blueprint("user", __name__)
schema = UserSchema()


@user_bp.route("/perfil", methods=["GET"])
@login_required
def profile():
    schema = UserSchema(exclude=["senha"])

    return success("Informações do usuário", data=schema.dump(current_user))


@user_bp.route("/perfil", methods=["PUT"])
@login_required
def update_user():
    data = request.get_json()

    user = UserService.update_user(current_user, data)

    return success("Usuário atualizado", data=schema.dump(user))