from typing import List, Union

from .base import CustomField
from ..utils.types import RawCustomField
from ..utils.validators import LabelsValidator


class LabelsField(CustomField):
    TYPE = "labels"
    VALIDATOR = LabelsValidator

    def get_value(self, raw_field: RawCustomField) -> List[str]:
        value_ids = raw_field['value']

        if not value_ids:
            return []
 
        options = raw_field['type_config']['options']

        def get_name_by_id(id: str) -> str:
            return next(filter(
                lambda option: option['id'] == id, options
            ))['label']

        return list(map(get_name_by_id, value_ids))

    def set_value(
        self, value: Union[str, List[str]], raw_field: RawCustomField
    ) -> None:
         
        options = raw_field['type_config']['options']
        valid_options = list(filter(
            lambda option: option['label'] in value, options
        ))

        previous_values = raw_field.get('value') or []

        raw_field['value'] = [ 
            *previous_values,
            *map(lambda option: option['id'], valid_options)
        ]
