import pytest
from pyclickup.utils.exceptions.fields import RequiredFieldMissing


def test_update__task_with_id__update_obj(
    monkeypatch, client_list_1, raw_task_for_client_1
):

    monkeypatch.setattr(
        "pyclickup.list.clickup_api.update_task", 
        lambda task_id, **kwargs: raw_task_for_client_1
    )

    task = client_list_1(dict(id="Some valid id", name="Old name"))
    task.update()

    assert task.name == "Client 1 Task"
    assert task.text == "Some text"

def test_update__task_without_id__raise_error(
    monkeypatch, client_list_1, raw_task_for_client_1
):

    monkeypatch.setattr(
        "pyclickup.list.clickup_api.update_task", 
        lambda task_id, **kwargs: raw_task_for_client_1
    )

    task = client_list_1()

    with pytest.raises(RequiredFieldMissing):
        task.update()
