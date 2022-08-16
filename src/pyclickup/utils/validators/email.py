import re
from typing import Any

from .string import StringValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class EmailValidator(StringValidator):
    EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    @classmethod
    def __is_good_email(cls, value: str) -> bool:
        return bool(re.fullmatch(cls.EMAIL_REGEX, value))

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field)

        if not cls.__is_good_email(value):
            raise ValidationError(f"Must be an email! Your value: {value}")
