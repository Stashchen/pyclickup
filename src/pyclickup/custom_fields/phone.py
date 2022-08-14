from .base import CustomField
from ..utils.validators import NumericStringValidator


class PhoneField(CustomField):
    TYPE = "phone"
    VALIDATOR = NumericStringValidator
