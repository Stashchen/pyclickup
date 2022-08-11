from typing import Any
from list import ClickUpList
from utils.types import RawCustomField
from .base import BaseValidator, ValidationError


class RelationValidator(BaseValidator):
    """
    Validates that only specific ClickUpList can be set to task, e.g.
    
    class ChildList(ClickUpList):
        name = TextField(field_name="Some text")

    class ParentList(ClickUpList):
        child = RelationField(ChildList, field_name="My child")

    >> parent = ParentList()
    >> child = ChildList()
    >> parent.child = child  # GOOD
    >> parent.child = "Test" # Error
    """

    @classmethod
    def _is_correct_relation_class(
        cls, 
        value: ClickUpList, 
        raw_field: RawCustomField
    ) -> bool:
        """
        Method that will check if value, that is wanted to be set is
        correct RelationField list class

        The idea behind this is that list_relationship type_config must
        have `subcategory_id` value that represents the id of related list.
        Related list value can also be grabbed from LIST_ID variable in 
        ClickUpList classes.

        So, summing up, if 

        raw_field.type_config.subcategory_id == value.__class__.LIST_ID
        
        so the value is good.
        """
        value_list_id = str(value.__class__.LIST_ID)
        list_id_from_field = raw_field["type_config"]["subcategory_id"]

        return value_list_id == list_id_from_field 

    @classmethod
    def validate(
        cls,
        value: Any,
        raw_field: RawCustomField
    ) -> None:
        super().validate(value, raw_field)
        
        if not isinstance(value, ClickUpList):
            raise ValidationError(
                "Value must be object of type/subtype ClickUpList"
            )

        value_class = value.__class__.__name__

        if not cls._is_correct_relation_class(value, raw_field):         
            raise ValidationError(
                f"You can't set {value_class} for {raw_field['name']} field "
            )

        if not value.id:
            raise ValidationError(
                f"{value_class} must have `id`. Please, create your object."
            )
