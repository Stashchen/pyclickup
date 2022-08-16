from typing import Any

from .base import BaseValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class NumberValidator(BaseValidator):
    """Validates that value is `float` or `int`."""

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        if type(value) not in [int, float]:
            raise ValidationError("Must be `int` or `float` value")

class PositiveNumberValidator(NumberValidator):
    """Validates that value is `float` or `int` that is >= 0."""

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field)

        if value < 0:
            raise ValidationError("Must be number that is >= 0")
