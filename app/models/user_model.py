from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email =  db.Column(db.String(120), unique=True, nullable=False)
    senha_hash =  db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return f"<Usuario id={self.id} nome={self.nome}>"