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
