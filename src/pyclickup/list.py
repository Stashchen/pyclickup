from __future__ import annotations
from functools import cached_property, lru_cache
from typing import Any, List, Union, Optional

from .services import clickup_api
from .services.cache import CustomFieldsCache, ClientListsRegistry
from .utils.types import RawTask, RawCustomField
 

class TaskIdNotFound(Exception):
    """Raised, when there is no `id` found in task object."""

class ClientListsLookup(type):
    """
    Metaclass that will store each client class to the registry.
    So, when a client define a class
    ```
    class ClientsClass(ClickUpList):
        ...fields
    ```
    the `ClientsClass` will be stored in the registry as 
    {
        client_list_name: client_list_class
    }
    """
    
    def __new__(cls, name, bases, attrs):
        cls = type.__new__(cls, name, bases, attrs)

        if bases: 
            ClientListsRegistry.update({
                name: cls 
                for base in bases
                if base == ClickUpList
            })

        return cls

class ClickUpList(metaclass=ClientListsLookup):
    """
    Base ClickUp list representation, that will have default ClickUp task
    properties. 

    This list has CRUD functionality that use ClickUpApi.

    This class is the base class for client ClickUp lists. E.g.
    ``` 
    class ClientClass(ClickUpList):
        field_1 = CustomField(field_name="Client Field Name")
    ``` 

    It will give the possibility to easily work with custom ClickUp lists.
    """
    LIST_ID = None

    def __init__(self, raw_task: Union[RawTask, dict]=dict()):
        self._raw_task = raw_task
        self._fields_cache = CustomFieldsCache()

    def __get_custom_fields_from_api(self) -> List[RawCustomField]:
        raw_payload = clickup_api.get_custom_fields(self.LIST_ID)
        return raw_payload['fields']

    @property
    def id(self) -> Optional[str]:
        return self._raw_task.get("id")

    @property
    def name(self) -> Optional[str]:
        return self._raw_task.get("name")

    @name.setter
    def name(self, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError("`name` attribute must be str")
        self._raw_task['name'] = value

    @property
    def url(self) -> Optional[str]:
        return self._raw_task.get("url")

    @cached_property
    def custom_fields(self) -> List[RawCustomField]:
        """
        Try to get custom fields from `raw_task`. If they are not found,
        they will be pulled from API.
        """
        custom_fields = self._raw_task.get('custom_fields')

        if custom_fields:
            return custom_fields

        return self.__get_custom_fields_from_api()

    @classmethod
    @lru_cache(maxsize=1)
    def get_all_tasks(cls) -> List[RawTask]:
        """Method that will fetch all the tasks from the current list."""
        page = 0  
        all_tasks = []

        while True:
            tasks = clickup_api.get_batch_tasks(cls.LIST_ID, page).get('tasks')

            if not tasks: break

            all_tasks.extend(tasks)

            if tasks and len(tasks) < 100: break

            page += 1

        return all_tasks 
    
    # CRUD functionality
    @classmethod
    def get_by_id(cls, task_id: str):
        """Class method, that will fetch task by its id."""
        raw_task = clickup_api.get_task(task_id=task_id)
        return cls(raw_task)

    @classmethod
    def get_by_name(cls, task_name: str):
        """Class method, that will fetch task by its name."""

        raw_task = next(filter(
            lambda task: task['name'] == task_name, cls.get_all_tasks()
        ), None)

        if not raw_task: return

        return cls(raw_task)

    def create(self):
        """
        Method, that will get current raw_task 
        values and push them to ClickUp.
        """
        custom_fields = self._fields_cache.get()
        body = dict(
            name=self.name,
            custom_fields=custom_fields
        )
        raw_task = clickup_api.create_task(self.LIST_ID, **body)
        self._raw_task = raw_task

    def update(self):
        """
        Method, that will update existed ClickUp task.
        It will
        1) Check task_id. If there is no id, so the task is not existe.
        2) Update base task field (Only name by now)
        3) Update custom fields
        """
        if not self.id:
            raise TaskIdNotFound("Can not update unexisted Task")

        body = dict(name=self.name)
        clickup_api.update_task(self.id, **body)
 
        custom_fields = self._fields_cache.get()

        if custom_fields:
            for field in custom_fields:
                clickup_api.set_custom_field(
                    task_id=self.id,
                    field_id=field['id'],
                    value=field['value']
                )
