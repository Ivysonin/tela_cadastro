from flask import Flask
from app.config import Config
from app.extensions import db, migrate, login_manager
from app.core.handlers import register_error_handlers


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.controllers.auth_controller import auth_bp
    from app.controllers.user_controller import user_bp
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    register_error_handlers(app)

    from app.models import user_model
    from app.models.user_model import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))
    
    return app