from datetime import date, datetime
from typing import Any

from .base import BaseValidator, ValidationError
from ..types import RawCustomField


class DateValidator(BaseValidator):
    """Validates that `value` is `datetime` or `date` value."""

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field)

        if not (type(value) in [datetime, date]):
            raise ValidationError(
                f"{raw_field['name']} must be `datetime` or `date`."
            )
