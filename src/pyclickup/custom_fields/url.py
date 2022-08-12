from .base import CustomField
from ..utils.validators import UrlValidator


class UrlField(CustomField):
    TYPE = "url"
    VALIDATOR = UrlValidator
 
