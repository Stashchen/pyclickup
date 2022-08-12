from typing import Any

from .base import ValidationError
from .string import StringValidator 
from ..types import RawCustomField


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
