from typing import Optional
from .base import CustomField
from utils.types import RawCustomField
from utils.validators import DropDownValidator


class DropDownField(CustomField):
    TYPE = 'drop_down'
    VALIDATOR = DropDownValidator

    def get_value(self, raw_field: RawCustomField) -> Optional[str]:
        orderindex = raw_field['value']

        if not orderindex:
            return

        options = raw_field['type_config']['options']
        good_option = next(filter(
            lambda option: option['orderindex'] == orderindex,
            options
        ))

        return good_option['name']

    def set_value(self, value: str, raw_field: RawCustomField) -> None:
        """
        value is the `name` variable of type_config >> options.
        """
        options = raw_field['type_config']['options']

        good_option = next(filter(
            lambda option:
            option['name'] == value,
            options
        ))
        
        raw_field['value'] = good_option['orderindex']

