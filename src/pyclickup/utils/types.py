from typing import Any, TypedDict, List, Optional


class RawCustomField(TypedDict):
    id: str
    type: str
    name: str
    type_config: dict
    value: Optional[Any]

class RawTask(TypedDict):
    id: str
    description: str
    status: dict
    url: str
    name: str
    type: str
    custom_fields: List[RawCustomField]

class FieldToUpdate(TypedDict):
    id: str
    value: Any
