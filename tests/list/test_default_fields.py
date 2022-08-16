import pytest
from datetime import datetime
from pyclickup.list import ReadOnlyTaskField
from pyclickup.utils.exceptions.fields import InvalidOption


# ID field
def test_get_id__exists__return_string(client_1_task):
    assert client_1_task.id == "client_1_task_id"

def test_get_id__no_data__return_none(client_1_task):
    assert client_1_task.id is None

def test_set_id__any_data__raise_error(client_1_task): 
    with pytest.raises(ReadOnlyTaskField):
        client_1_task.id = "New id"

# Name field
def test_get_name__exists__return_string(client_1_task):
    assert client_1_task.name == "Client 1 Task"

def test_get_name__no_data__return_none(client_1_task):
    assert client_1_task.name is None

def test_set_name__string__update_field(client_1_task): 
    client_1_task.name = "New name" 
    assert client_1_task.name == "New name"

def test_set_name__not_string__raise_error(client_1_task):
    with pytest.raises(TypeError):
        client_1_task.name = 123

# Status field
def test_get_status__exists__return_string(client_1_task):
    assert client_1_task.status == "Some status"

def test_get_status__no_data__return_none(client_2_task):
    assert client_2_task.status is None

def test_set_status__valid_option__update_status(
    monkeypatch, client_1_task, fake_statuses
):
    monkeypatch.setattr(
        "pyclickup.list.clickup_api.get_list",
        lambda list_id: dict(statuses=fake_statuses) 
    )

    client_1_task.status = "New Status #1"
    assert client_1_task.status == "New status #1"

def test_set_status__invalid_option__raise_error(
    monkeypatch, client_1_task, fake_statuses
):
    monkeypatch.setattr(
        "pyclickup.list.clickup_api.get_list",
        lambda list_id: dict(statuses=fake_statuses) 
    )

    with pytest.raises(InvalidOption):
        client_1_task.status = "Invalid status"

# Description field
def test_get_description__exists__return_string(client_1_task):
    assert client_1_task.description == "Some description"

def test_get_description__no_data__return_none(client_1_task):
    task = client_1_task()

    assert task.description is None

def test_set_description__string__update_field(client_1_task): 
    task = client_1_task()
    task.description = "New description"
    
    assert task.description == "New description"

def test_set_description__not_string__raise_error(client_1_task):
    task = client_1_task()

    with pytest.raises(TypeError):
        task.description = 123

# Due date
def test_get_due_date__exists__return_datetime(client_1_task):
    assert client_1_task.due_date == datetime(2022, 12, 12)

def test_get_due_date__no_data__return_none(client_2_task):
    assert client_2_task.due_date is None 

def test_set_due_date__datetime__update_field(client_1_task):
    client_1_task.due_date = datetime(2022, 11, 11)
    assert client_1_task.due_date == datetime(2022, 11, 11)

def test_set_due_date__not_datetime__raise_error(client_1_task):
    with pytest.raises(TypeError):
        client_1_task.due_date = "Invalid data"

# URL field
def test_get_url__exists__return_string(client_1_task):
    assert client_1_task.url == "https://app.clickup.com/t/client_1_task_id"

def test_get_url__no_data__return_none(client_1_task):
    assert client_1_task.url is None

def test_set_url__any_data__raise_error(client_1_task): 
    with pytest.raises(ReadOnlyTaskField):
        client_1_task.url = "New url"
