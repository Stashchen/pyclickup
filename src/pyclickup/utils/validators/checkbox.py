from typing import Any

from .base import BaseValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class CheckboxValidator(BaseValidator):
    """Validates that only `True`/`False` can be set."""

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field)

        if not (value is True or value is False):
            raise ValidationError(
                f"{raw_field['name']} must be `True` or `False`."
            )
