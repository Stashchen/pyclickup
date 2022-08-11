from typing import Any
from utils.types import RawCustomField
from .base import ValidationError


class StringValidator:
    """Validates that value is `str` type."""
    
    @classmethod
    def validate(
        cls,
        value: Any,
        raw_field: RawCustomField
    ) -> None:
        if not isinstance(value, str):
            raise ValidationError("Must be string")
