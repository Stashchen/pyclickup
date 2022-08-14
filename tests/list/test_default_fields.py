import pytest
from pyclickup.list import ReadOnlyTaskField


# ID field
def test_get_id__exists__return_string(client_1_task):
    assert client_1_task.id == "client_1_task_id"

def test_get_id__no_data__return_none(client_list_1):
    task = client_list_1()
    assert task.id is None

def test_set_id__any_data__raise_error(client_list_1): 
    task = client_list_1()

    with pytest.raises(ReadOnlyTaskField):
        task.id = "New id"


# Name field
def test_get_name__exists__return_string(client_1_task):
    assert client_1_task.name == "Client 1 Task"

def test_get_name__no_data__return_none(client_list_1):
    task = client_list_1()

    assert task.name is None

def test_set_name__string__update_field(client_list_1): 
    task = client_list_1()
    task.name = "New name"
    
    assert task.name == "New name"

def test_set_name__not_string__raise_error(client_list_1):
    task = client_list_1()

    with pytest.raises(TypeError):
        task.name = 123


# Description field
def test_get_description__exists__return_string(client_1_task):
    assert client_1_task.description == "Some description"

def test_get_description__no_data__return_none(client_list_1):
    task = client_list_1()

    assert task.description is None

def test_set_description__string__update_field(client_list_1): 
    task = client_list_1()
    task.description = "New description"
    
    assert task.description == "New description"

def test_set_description__not_string__raise_error(client_list_1):
    task = client_list_1()

    with pytest.raises(TypeError):
        task.description = 123


# URL field
def test_get_url__exists__return_string(client_1_task):
    assert client_1_task.url == "https://app.clickup.com/t/client_1_task_id"

def test_get_url__no_data__return_none(client_list_1):
    task = client_list_1()
    assert task.url is None

def test_set_url__any_data__raise_error(client_list_1): 
    task = client_list_1()

    with pytest.raises(ReadOnlyTaskField):
        task.url = "New url"
