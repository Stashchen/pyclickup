from .number import NumberField
from ..utils.validators import PositiveNumberValidator


class CurrencyField(NumberField):
    TYPE = "currency"
    VALIDATOR = PositiveNumberValidator
