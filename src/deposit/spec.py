from marshmallow import Schema, fields

from deposit.utils import DATE_FORMAT


def validate_value_range(min_value: float, max_value: float):
    def inner(value: float):
        return min_value <= value <= max_value
    return inner


class DepositRequestSchema(Schema):
    date = fields.Date(format=DATE_FORMAT, required=True)
    periods = fields.Integer(
        required=True, validate=validate_value_range(1, 60)
    )
    amount = fields.Integer(
        required=True,
        validate=validate_value_range(10_000, 3_000_000)
    )
    rate = fields.Float(required=True, validate=validate_value_range(1, 8))


class DepositResponseSchema(Schema):
    additionalProperties = fields.Float()
