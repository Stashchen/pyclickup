import pytest

@pytest.fixture()
def fake_statuses():
    return [
        dict(status="New status #1"),
        dict(status="New status #2")
    ]
