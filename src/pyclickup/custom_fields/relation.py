from typing import Type, List, Union 
from .base import CustomField
from ..list import ClickUpList
from ..services import clickup_api
from ..services.cache import ClientListsRegistry
from ..utils.types import RawCustomField
from ..utils.validators import RelationValidator


class ClientListNotFound(Exception):
    """Raised when client list class not found."""

class RelationField(CustomField):
    TYPE = "list_relationship"
    VALIDATOR = RelationValidator

    def __init__(self, related_list: Union[str, Type[ClickUpList]], field_name: str):
        super().__init__(field_name)
        self._related_list = related_list
        
    @property
    def related_list(self):
        """
        Property that will grab correct client list from registry on runtime.
        """
        related_list = self._related_list

        if isinstance(related_list, str):
            related_list_name = related_list
            related_list = ClientListsRegistry.get(related_list)
            if not related_list:
                raise ClientListNotFound(
                    f"There is no such class: {related_list_name}"
                )

        return related_list

    def set_value(
        self, 
        value: ClickUpList,
        raw_field: RawCustomField
    ) -> None:
        current_values = raw_field.get("value")

        if not current_values:
            current_values = []

        if current_values:
            existed_ids = list(map(lambda item: item['id'], current_values))
            if value.id in existed_ids:
                return

        raw_field['value'] = [*current_values, dict(id=value.id)]

    def get_value(self, raw_field: RawCustomField) -> List[ClickUpList]:
        values = raw_field.get("value")

        if values is None:
            return []

        def build_correct_task(value: dict) -> ClickUpList:
            raw_task = clickup_api.get_task(task_id=value['id'])
            return self.related_list(raw_task)

        return list(map(
            lambda value:
            build_correct_task(value),
            values
        ))
