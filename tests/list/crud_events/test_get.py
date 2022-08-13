import pytest
from pyclickup.list import TaskFromWrongList, ClickUpList


def test_get_by_id__good_id__create_obj(
    monkeypatch, client_list_1, raw_task_for_client_1
):

    monkeypatch.setattr(
        "pyclickup.list.clickup_api.get_task", 
        lambda task_id: raw_task_for_client_1
    )
    
    new_task = client_list_1.get_by_id("Good Id")
    assert new_task.id == client_list_1(raw_task_for_client_1).id

def test_get_by_id__wrong_list_id__raise_error(
    monkeypatch, client_list_1, raw_task_for_client_1
):
    raw_task_for_client_1['list']['id'] = "another_list_id" 

    monkeypatch.setattr(
        "pyclickup.list.clickup_api.get_task", 
        lambda task_id: raw_task_for_client_1
    )
    
    with pytest.raises(TaskFromWrongList):
        client_list_1.get_by_id("Good Id")

def test_get_by_id__bad_id__return_none(
    monkeypatch, client_list_1
):
    monkeypatch.setattr(
        "pyclickup.list.clickup_api.get_task", 
        lambda task_id: None
    )

    new_task = client_list_1.get_by_id("Invalid Id")
    assert new_task is None


def test_get_by_name__good_name__create_obj(
    monkeypatch, client_list_1, raw_task_for_client_1
):
    monkeypatch.setattr(
        ClickUpList,
        "_get_all_tasks_as_chunks",
        lambda: [[raw_task_for_client_1]]
    )

    new_task = client_list_1.get_by_name("Client 1 Task")

    assert new_task.id == "client_1_task_id"

def test_get_by_name__bad_name__return_none(
    monkeypatch, client_list_1, raw_task_for_client_1
):
    monkeypatch.setattr(
        ClickUpList,
        "_get_all_tasks_as_chunks",
        lambda: [[raw_task_for_client_1]]
    )

    new_task = client_list_1.get_by_name("Invalid Name")

    assert new_task is None
