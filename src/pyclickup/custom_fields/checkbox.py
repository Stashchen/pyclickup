from .base import CustomField
from utils.types import RawCustomField
from utils.validators import CheckboxValidator


class CheckboxField(CustomField):
    TYPE = "checkbox"
    VALIDATOR = CheckboxValidator
    
    def get_value(self, raw_field: RawCustomField) -> bool:
        value = raw_field.get("value")

        if not value:
            return False

        return True if value == "true" else False 

