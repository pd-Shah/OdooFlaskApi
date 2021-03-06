from marshmallow import Schema, fields


class LoginUser(Schema):
    username = fields.Str(required=True, )
    password = fields.Str(required=True, )


class PortalUser(Schema):
    name = fields.Str(required=True, )
    login = fields.Str(required=True, )
    phone_number = fields.Str(required=True, )
    password = fields.Str(required=True, )
    country_phone_code = fields.Str(required=True, )


