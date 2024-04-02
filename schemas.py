from marshmallow import Schema, fields

class CarSchema(Schema):
    id = fields.Str(dump_only=True)
    model = fields.Str(required=True)
    make = fields.Str(required=True)

class SaleReceiptsSchema(Schema):
    id = fields.Str(dump_only=True)
    condition = fields.Str(required=True)
    color = fields.Str(required=True)
    car = fields.Nested(CarSchema, required=True)
    salesman = fields.Str(required=True)
    sale = fields.Int(required=True)
