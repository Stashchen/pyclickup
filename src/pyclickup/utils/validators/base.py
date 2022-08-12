from abc import abstractmethod, ABC
from typing import Any

from ..types import RawCustomField


class ValidationError(Exception):
    """Raised by Validator when condition is not matched."""


class BaseValidator(ABC):
    """Interface for future Validators."""

    @classmethod
    @abstractmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        ...

class ForbidValuesValidator(BaseValidator):
    """Will not allow to set any values."""

    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        if value:
            raise ValidationError(
                "You are not allowed to set any value for that field!"
            )
