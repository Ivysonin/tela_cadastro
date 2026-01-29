from flask import Blueprint, request
from flask_login import login_required
from app.services.auth_service import AuthService
from app.schemas.user_schema import UserSchema
from app.core.response import success


auth_bp = Blueprint("auth", __name__)
schema = UserSchema()


@auth_bp.route('/register', methods=["POST"])
def register_user():
    data = request.get_json()

    user = AuthService.register(data)

    return success("Usuário registrado com sucesso", data=schema.dump(user))


@auth_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    AuthService.login(data)

    return success("Login realizado com sucesso")


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout_user():
    AuthService.logout()
    return success("", status=204)