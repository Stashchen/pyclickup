from typing import Any

from .base import BaseValidator, ValidationError
from ..types import RawCustomField


class StringValidator(BaseValidator):
    """Validates that value is `str` type."""
    
    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        if not isinstance(value, str):
            raise ValidationError("Must be string")

class NumericStringValidator(StringValidator):
    """Validate that value is `str` type but only with numbers [0-9]."""

    @classmethod
    def validate(cls, value: str, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field)

        if not value.isnumeric():
            raise ValidationError("Must be string with numbers [0-9]")





