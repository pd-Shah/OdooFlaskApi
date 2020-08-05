from marshmallow import Schema, fields


class User(Schema):
    name = fields.Str()
