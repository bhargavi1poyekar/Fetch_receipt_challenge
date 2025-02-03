from marshmallow import Schema, fields, validate, validates, ValidationError
from marshmallow.validate import Regexp
from datetime import datetime

class ItemSchema(Schema):
    shortDescription = fields.String(
        required=True,
        validate=Regexp(r"^[\w\s\-]+$", error="Invalid short description format.")
    )
    price = fields.String(
        required=True,
        validate=Regexp(r"^\d+\.\d{2}$", error="Invalid price format, expected a value like '6.49'.")
    )

class ReceiptSchema(Schema):
    retailer = fields.String(
        required=True,
        validate=Regexp(r"^[\w\s\-\&]+$", error="Invalid retailer name format.")
    )
    purchaseDate = fields.String(
        required=True,
        format='date',
        example="2022-01-01"
    )
    purchaseTime = fields.String(
        required=True,
        format='time',
        example="13:01"
    )
    items = fields.List(fields.Nested(ItemSchema), required=True, validate=lambda lst: len(lst) > 0)
    total = fields.String(
        required=True,
        validate=Regexp(r"^\d+\.\d{2}$", error="Invalid total format, expected a value like '6.49'.")
    )

    @validates('purchaseDate')
    def validate_purchase_date(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValidationError("Invalid date. It should be in YYYY-MM-DD format. Month should be between 01-12. ")

    
    @validates('purchaseTime')
    def validate_purchase_time(self, value):
        try:
            time_obj = datetime.strptime(value, '%H:%M')
            hours, minutes = time_obj.hour, time_obj.minute
            if hours > 23 or minutes > 59:
                raise ValidationError("Invalid time. Hours should be between 00 and 23, and minutes should be between 00 and 59.")
        except ValueError:
            raise ValidationError("Invalid time format. Expected 'HH:MM' in 24-hour format.")

    @validates('items')
    def validate_items(self, value):
        if len(value) == 0:
            raise ValidationError("Items list cannot be empty.")