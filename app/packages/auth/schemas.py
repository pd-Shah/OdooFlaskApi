from marshmallow import Schema, fields


class LoginUser(Schema):
    username = fields.Str()
    password = fields.Str()


class PortalUser(Schema):
    name = fields.Str()
    login = fields.Str()
    email = fields.Email()
