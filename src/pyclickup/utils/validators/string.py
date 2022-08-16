from typing import Any

from .base import BaseValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class StringValidator(BaseValidator):
    """Validates that value is `str` type."""
    
    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        if not isinstance(value, str):
            raise ValidationError("Must be string")

