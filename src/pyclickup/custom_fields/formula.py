from .base import CustomField
from ..utils.validators import ForbidValuesValidator


class FormulaField(CustomField):
    """
    Formula fields allow you ONLY to get value. They will set automatically.
    """
    TYPE = "formula"
    VALIDATOR = ForbidValuesValidator

