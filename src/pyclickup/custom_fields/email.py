from .base import CustomField
from utils.validators import EmailValidator


class EmailField(CustomField):
    TYPE = "email"
    VALIDATOR = EmailValidator
