from requests import Session
from utils.datastructures import Singleton


SAFE_METHODS = ("get", "head", "option")
VALID_METHODS = (*SAFE_METHODS, "post", "put", "patch", "delete")

class BaseApi(Session, Singleton): 
    """
    Base API class that will be used for different 3rd party APIs.

    Each subclass API will be created once (using Singleton) and can
    be used globally.
    """

    endpoint = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self._perform_auth()

    def _perform_auth(self):
        """
        Interface for API authentication.
        Must be implemented in subclasses.
        """

