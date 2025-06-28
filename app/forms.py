from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import data_required, Email, ValidationError, Length
from app.models import Users
from app import db, bcrypt


class UsersForm(FlaskForm):
    nome = StringField('Nome', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required(), Length(min=8)])
    btn_enviar = SubmitField('Enviar')

    def validate_email(self, email):
        if Users.query.filter_by(email=email.data).first():
            raise ValidationError('Usuário já cadastrado com esse E-mail!!!')

    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8')).decode('utf-8')

        user = Users(
            nome = self.nome.data,
            email = self.email.data,
            senha = senha
        )
        db.session.add(user)
        db.session.commit()
        return user