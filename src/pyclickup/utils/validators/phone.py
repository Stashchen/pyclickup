from typing import Any

from .string import StringValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class PhoneValidator(StringValidator):
    """
    Validates that value is `str` with following rules:
    - Must start with `+`;
    - Other symbols are numbers or spaces.
    """

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field) 

        phone_number = value[1:].replace(' ', '') 

        if not all([value.startswith('+'), phone_number.isnumeric()]):
            raise ValidationError(
                "Must be string that includes numbers, "
                "spaces and `+` at the beginning\n"
                "Example: '+123 456 7890'"
            )
