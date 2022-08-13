import pytest


def test_create__good_data__create_obj(
    monkeypatch, client_list_1, raw_task_for_client_1
):

    monkeypatch.setattr(
        "pyclickup.list.clickup_api.create_task", 
        lambda list_id, **kwargs: raw_task_for_client_1
    )

    task = client_list_1()
    task.name = "New Task"
    
    task.create()

    assert task.id == "client_1_task_id"
