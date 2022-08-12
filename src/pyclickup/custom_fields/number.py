from .base import CustomField
from ..utils.validators import NumberValidator


class NumberField(CustomField):
    TYPE = "number"
    VALIDATOR = NumberValidator
