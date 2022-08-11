import os
from requests import Response
from utils.decorators import resp_to_json
from utils.exceptions import AuthTokenMissing
from .base import BaseApi


os.environ["CLICKUP_AUTH_TOKEN"] = "pk_48036859_VHYZAJWVA6L8IW6U9W6P6FDTRA1K646L"


class ClickUpApi(BaseApi):
    """Class that proxy the ClickUp api."""
    
    endpoint = "https://api.clickup.com/api/v2"
    

    def _perform_auth(self) -> None:
        """Attaches ClickUp API token to API headers."""

        token = os.environ.get("CLICKUP_AUTH_TOKEN")

        if not token:
            raise AuthTokenMissing(
                "Please, set `CLICKUP_AUTH_TOKEN` in your environment."
            )

        self.headers.update({
            "Authorization": token
        })

    @resp_to_json
    def get_task(self, task_id: str) -> Response:
        return self.get(f"{self.endpoint}/task/{task_id}")

    @resp_to_json
    def create_task(self, list_id: str, **kwargs) -> Response:
        return self.post(f"{self.endpoint}/list/{list_id}/task", json=kwargs)

    @resp_to_json
    def update_task(self, task_id: str, **kwargs) -> Response:
        return self.put(f"{self.endpoint}/task/{task_id}", json=kwargs)

    @resp_to_json
    def get_custom_fields(self, list_id: str) -> Response:
        return self.get(f"{self.endpoint}/list/{list_id}/field")

    @resp_to_json
    def set_custom_field(self, task_id: str, field_id: str, **kwargs) -> Response:
        return self.post(f"{self.endpoint}/task/{task_id}/field/{field_id}", json=kwargs)

