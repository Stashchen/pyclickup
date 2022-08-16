from .base import CustomField
from ..utils.validators import PhoneValidator


class PhoneField(CustomField):
    TYPE = "phone"
    VALIDATOR = PhoneValidator
