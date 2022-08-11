from utils.validators import PositiveNumberValidator
from .base import CustomField


class CurrencyField(CustomField):
    TYPE = "currency"
    VALIDATOR = PositiveNumberValidator
