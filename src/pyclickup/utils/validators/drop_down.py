from typing import Any, List

from .string import StringValidator
from ..exceptions.validators import ValidationError
from ..types import RawCustomField


class DropDownValidator(StringValidator):
    """
    Validates that value is the correct `name` variable from
    field's type_config options.
    """

    @classmethod
    def __has_good_option(cls, value: str, options: List[dict]) -> bool:
        good_option = next(filter(
            lambda option: option['name'] == value,
            options
        ), None)
        return good_option is not None
                
    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        super().validate(value, raw_field)

        options = raw_field['type_config']['options']

        if not cls.__has_good_option(value, options):
            valid_names = list(map(lambda option: option['name'], options))
            raise ValidationError(
                "Invalid option!\n"
                f"Your value: {value}\n"
                f"Possible values: {valid_names}"
            )
