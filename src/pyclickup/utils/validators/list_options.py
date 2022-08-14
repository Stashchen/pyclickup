from typing import Any, List, Union

from .base import BaseValidator, ValidationError
from ..types import RawCustomField


class OptionsListValidator(BaseValidator):
    """
    Validates that value is one of the `options` in `type_config`.

    Valid setter options:
    - task.attr = "valid_option_as_str"
    - task.attr = ["valid_option_as_str_1", "valid_option_as_str_1"]
    """
    NAME_KEY = None

    @classmethod
    def __has_good_options(
        cls, value: Union[str, List[str]], valid_options_names: List[str]
    ) -> bool:
        return all([name in valid_options_names for name in value])
                
    @classmethod
    def validate(cls, value: Any, raw_field: RawCustomField) -> None:
        
        if not (isinstance(value, list) or isinstance(value,  str)):
            raise ValidationError("Must be `str` or `list`")

        if isinstance(value, str):
            value = [value]

        options = raw_field['type_config']['options']
        valid_names = list(map(lambda option: option[cls.NAME_KEY], options))

        if not cls.__has_good_options(value, valid_names):
            raise ValidationError(
                "Invalid option(s)!\n"
                f"Your value(s): {value}\n"
                f"Possible values: {valid_names}"
            )
