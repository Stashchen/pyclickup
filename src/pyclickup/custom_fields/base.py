from typing import Any, Optional, Type

from ..list import ClickUpList
from ..utils.types import RawCustomField
from ..utils.validators import StringValidator


class CustomFieldNotFound(Exception):
    """Raised if raw custom field not found in raw clickup list."""

class CustomFieldIsNull(Exception):
    """Raised when None is set to required field."""

class CustomField:
    """
    Descriptor class that will set the workflow with ClickUp task's custom
    fields data.

    This workflow is based on 2 main ideas:
    1) __get__ method MUST return simple humanreadable value
    2) __set__ method MUST get simple humanreadable value that will be
       validated by CustomField VALIDATOR

    It will give a possibility to easily work with custom fields.

    This class is a base CustomField. There are also many others subclasses
    that represent different ClickUp custom fields (e.g. TextField, 
    NumberField, RelationField, DropDownField, etc.)

    There is one important pre-get/set workflow. Before working with attribute, 
    following steps will run on our `instance` (class, that will use CustomField):
    1) Check that `instance` is `ClickUpList`
    2) Check that `CustomField.field_name` == `instance.name`  
    3) Check that `CustomField.TYPE` == `instance.type`
    """
    TYPE = None
    VALIDATOR = StringValidator

    def __init__(self, field_name: str, required: bool=False):
        self.field_name = field_name
        self.required = required

    def __get__(self, instance: Any, instance_type: Type) -> Any:
        """
        Descriptor GET method that will:
        1) Do pre-get workflow (check class docstring)
        2) Run getter method (get_value)
        """
        raw_field = self._raw_field(instance)
        return self.get_value(raw_field)

    def __set__(self, instance: ClickUpList, value: Any) -> None:
        """
        Descriptor SET method that will:
        1) Check if there is a value and if the field is not
           required we can set None.
        2) Do pre-set workflow (check class docstring)
        3) Validate value to be the right type
        4) Run setter method (set_value)
        5) Store new value in cache
        """

        if value is None:
            if self.required:
                return 
            raise CustomFieldIsNull(f"`{self.field_name}` can not be None")

        raw_field = self._raw_field(instance)
        self.__validate_value(value, raw_field)
        self.set_value(value, raw_field)
        self.__store_value_in_cache(instance, raw_field)

    def get_value(self, raw_field: RawCustomField) -> Optional[Any]:
        """
        Getter that will return humanreadable value from raw dict-like 
        custom field

        By default it will return raw custom field's `value` attr.
        Can be implemented in subclasses
        """
        return raw_field.get('value')

    def set_value(
        self, value: Any, raw_field: RawCustomField
    ) -> None:
        """
        Setter that will set correct value based on humanreadable `value`.

        By default it will set `value` to the raw custom field's `value` attr.
        Can be implemented in subclasses
        """
        raw_field['value'] = value


    def __validate_value(
            self,
            value: Any,
            raw_field: RawCustomField
        ) -> None:
        """
        Method that will invoke specific validation for current class.
        This method is used BEFORE setting the attribute.
        """

        self.VALIDATOR.validate(value, raw_field)

    def _raw_field(self, instance: Any) -> RawCustomField:
        """
        Pre-get/set workflow implementation.
        Do following steps:
        1) Check that `instance` is `ClickUpList`
        2) Check that `CustomField.field_name` == `instance.name`  
        3) Check that `CustomField.TYPE` == `instance.type`
        4) Return good custom field or raise error
        """
        instance = self.__check_instance_type(instance) 
        field = self.__get_field_by_name_and_type(instance)

        if not field:
            raise CustomFieldNotFound(
                "There is no such field with\n"
                f"- type: {self.TYPE}\n"
                f"- name: {self.field_name}"
            )

        return field

    def __check_instance_type(self, instance: Any) -> ClickUpList:
        if not isinstance(instance, ClickUpList):
            raise TypeError("Instance must be `ClickUpList`")
        return instance

    def __get_field_by_name_and_type(
        self, instance: ClickUpList
    ) -> Optional[RawCustomField]:
        return next(filter(
            lambda field: 
            field['name'] == self.field_name and  
            field['type'] == self.TYPE,
            instance.custom_fields
        ), None)

    def __store_value_in_cache(
        self,
        instance: ClickUpList,
        raw_field: RawCustomField
    ) -> None:
        id = raw_field['id']
        value = raw_field.get('value')
 
        if not value: return
        
        if self.TYPE == 'list_relationship':
            only_ids = list(map(lambda item: item['id'], value))
            value = dict(add=only_ids)
        instance._fields_cache.add(field_id=id, value=value)


