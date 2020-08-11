from marshmallow import Schema, fields


class PortalUser(Schema):
    name = fields.Str()
    login = fields.Str()
    email = fields.Email()
