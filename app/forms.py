from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, Email
from app.models import Users
from app import db


class UsersForm(FlaskForm):
    nome = StringField('Nome', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    btn_enviar = SubmitField('Enviar')

    def save(self):
        user = Users(
            nome = self.nome.data,
            email = self.email.data
        )
        db.session.add(user)
        db.session.commit()