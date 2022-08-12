from typing import Any, TypedDict, List


class PostCustomField(TypedDict):
    id: str
    value: str

class CustomFieldsCache:
    """
    Class that will store all new custom_fields to perform custom fields
    update later.

    It will store the values after we set correct value for that, e.g.
    ```
    MyClickUpList.attr = <New Value>
    ```
    """

    def __init__(self):
        self._storage = [] 

    def add(self, field_id: str, value: Any):
        self._storage.append(PostCustomField(
            id=field_id,
            value=value
        ))

    def get(self) -> List[PostCustomField]:
        result = self._storage[:]
        self.clear()
        return result

    def clear(self):
        self._storage.clear()


class ClientListsRegistry:
    """
    Simple cache storage that will store all of the client's 
    lists names and classes at the beginning of the runtime.
    """
    _storage = {}
    
    @classmethod
    def get(cls, list_name: str):
        return cls._storage.get(list_name, None)

    @classmethod
    def set(cls, list_name: str, value):
        cls._storage[list_name] = value

    @classmethod
    def update(cls, clients_lists: dict):
        cls._storage.update(clients_lists)
