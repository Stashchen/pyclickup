import os
import pytest

from pyclickup.services.clickup import ClickUpApi
from pyclickup.utils.exceptions.http import AuthTokenMissing


def test_perform_auth__no_token__error_raised():
    token = os.environ["CLICKUP_AUTH_TOKEN"]  

    del os.environ["CLICKUP_AUTH_TOKEN"]

    with pytest.raises(AuthTokenMissing):
        ClickUpApi()

    os.environ["CLICKUP_AUTH_TOKEN"] = token
