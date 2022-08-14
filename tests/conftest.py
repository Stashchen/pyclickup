import json
import pytest

from pyclickup import ClickUpList
from pyclickup.custom_fields import *


@pytest.fixture
def client_list_1():

    class ClientListOne(ClickUpList):
        LIST_ID = "client_1_list_id"

        short_text = ShortTextField(field_name="Short Text", required=True)
        drop_down = DropDownField(field_name="Drop Down")
        formula = FormulaField(field_name="Formula")
        number = NumberField(field_name="Number")
        labels = LabelsField(field_name="Labels")
        text = TextField(field_name="Text")
        currency = CurrencyField(field_name="Currency")
        location = LocationField(field_name="Location")
        checkbox = CheckboxField(field_name="Checkbox")
        date = DateField(field_name="Date")
        email = EmailField(field_name="Email")
        phone = PhoneField(field_name="Phone")
        link = UrlField(field_name="Url")

        clients_2 = RelationField(
            "ClientListTwo", field_name="Client 2 realtion"
        )

    return ClientListOne

@pytest.fixture
def client_list_2():

    class ClientListTwo(ClickUpList):
        LIST_ID = "client_2_list_id"

    return ClientListTwo

@pytest.fixture
def raw_task_for_client_1():
    with open("tests/test_data/client_raw_task_1.json") as f:
        yield json.loads(f.read())

@pytest.fixture
def raw_task_for_client_2():
    with open("tests/test_data/client_raw_task_2.json") as f:
        yield json.loads(f.read())

@pytest.fixture
def client_1_task(client_list_1, raw_task_for_client_1):
    return client_list_1(raw_task_for_client_1)

@pytest.fixture
def client_2_task(client_list_2, raw_task_for_client_2):
    return client_list_2(raw_task_for_client_2)

@pytest.fixture
def client_1_empty_task(monkeypatch, client_list_1, raw_task_for_client_1):
    """Will include custom fields but without `value`s"""

    for custom_field in raw_task_for_client_1['custom_fields']:
        if 'value' in custom_field:
            del custom_field['value']

    monkeypatch.setattr(
        "pyclickup.ClickUpList.custom_fields",
        raw_task_for_client_1['custom_fields']
    )

    return client_list_1(raw_task_for_client_1)
