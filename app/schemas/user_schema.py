from marshmallow import Schema, fields, validates, ValidationError
import re


class UserSchema(Schema):
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True)


    @validates("nome")
    def validate_nome(self, value, **kwargs):
        if not re.match(r"^[A-Za-zÀ-ÿ\s]{3,}$", value):
            raise ValidationError("Nome inválido: mínimo 3 letras")

    @validates("senha")
    def validate_senha(self, value, **kwargs):
        if len(value) < 6:
            raise ValidationError("A nova senha deve ter no mínimo 6 caracteres")