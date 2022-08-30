from requests import Response
from typing import Callable
from .exceptions.http import BadRequest


def resp_to_json(func: Callable) -> Callable:
    """
    Check if the return value is `Response` and check if
    status code is 2xx. If it is not 2xx, BadRequest will be raises.
    """
    def wrapper(*args, **kwargs) -> dict:
        resp = func(*args, **kwargs)

        if not isinstance(resp, Response):
            return resp
        
        if resp.ok:
            return resp.json()

        raise BadRequest(f"Status {resp.status_code}\nContent: {resp.content}")
    return wrapper
