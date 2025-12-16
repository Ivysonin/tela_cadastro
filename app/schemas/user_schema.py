from marshmallow import Schema, fields


class UserSchema(Schema):
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True)