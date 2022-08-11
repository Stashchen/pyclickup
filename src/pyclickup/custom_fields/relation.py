from typing import Type, List
from list import ClickUpList
from .base import CustomField
from utils.types import RawCustomField
from utils.validators import RelationValidator

from services import clickup_api


class RelationField(CustomField):
    TYPE = "list_relationship"
    VALIDATOR = RelationValidator

    def __init__(self, related_list: Type[ClickUpList], field_name: str):
        super().__init__(field_name)
        self._related_list = related_list

    def set_value(
        self, 
        value: ClickUpList,
        raw_field: RawCustomField
    ) -> None:
        current_values = raw_field["value"] 

        if not current_values:
            current_values = []

        raw_field['value'] = [*current_values, dict(id=value.id)]

    def get_value(self, raw_field: RawCustomField) -> List[ClickUpList]:
        values = raw_field.get("value")

        if not values:
            return []

        def build_correct_task(value: dict) -> ClickUpList:
            raw_task = clickup_api.get_task(task_id=value['id'])
            return self._related_list(raw_task)

        return list(map(
            lambda value:
            build_correct_task(value),
            values
        ))
