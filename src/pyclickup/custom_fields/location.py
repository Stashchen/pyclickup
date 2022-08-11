from typing import Optional
from utils.types import RawCustomField
from .base import CustomField

from services import geo_grabber


class LocationField(CustomField):
    TYPE = "location"

    def set_value(self, value: str, raw_field: RawCustomField) -> None:
        location = geo_grabber.search(value)
        raw_field['value'] = location.to_dict()

    def get_value(self, raw_field: RawCustomField) -> Optional[str]:
        value = raw_field.get("value")
        
        if not value:
            return

        return value['formatted_address']

