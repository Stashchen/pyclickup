from typing import Any
from utils.types import RawCustomField
from .base import ValidationError
from .string import StringValidator 


class UrlValidator(StringValidator):
    """Validates that string is URL."""
    
    @classmethod
    def validate(
        cls,
        value: Any,
        raw_field: RawCustomField
    ) -> None:
        super().validate(value, raw_field)

        if not value.startswith('http'):
            raise ValidationError(f"Must be a good url! Your value: {value}")
