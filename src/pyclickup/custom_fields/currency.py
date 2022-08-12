from .base import CustomField
from ..utils.validators import PositiveNumberValidator


class CurrencyField(CustomField):
    TYPE = "currency"
    VALIDATOR = PositiveNumberValidator
