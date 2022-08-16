import re
from typing import Any

from .string import StringValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class UuidValidator(StringValidator):
    """Validates that string is UUID."""

    UUID_REGEX = r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}$"

    @classmethod
    def __is_good_uuid(cls, value: str) -> bool:
        return bool(re.fullmatch(cls.UUID_REGEX, value))

    @classmethod
    def validate(
        cls,
        value: Any,
        raw_field: RawCustomField
    ) -> None:
        super().validate(value, raw_field)

        if not cls.__is_good_uuid(value):
            raise ValidationError(
                f"Must be a UUID string! Your value:  {value}"
            )
