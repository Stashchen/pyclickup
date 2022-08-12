from abc import abstractmethod, ABC
from typing import Any

from ..types import RawCustomField


class ValidationError(Exception):
    """Raised by Validator when condition is not matched."""


class BaseValidator(ABC):
    """Interface for future Validators."""

    @classmethod
    @abstractmethod
    def validate(
        cls,
        value: Any,
        raw_field: RawCustomField
    ) -> None:
        ...
