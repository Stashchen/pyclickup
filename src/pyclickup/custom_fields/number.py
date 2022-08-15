from typing import Optional
from .base import CustomField
from ..utils.types import RawCustomField
from ..utils.validators import NumberValidator


class NumberField(CustomField):
    TYPE = "number"
    VALIDATOR = NumberValidator

    def get_value(self, raw_field: RawCustomField) -> Optional[float]:
        value =  raw_field.get("value")
        
        if not value:
            return

        return float(value)
