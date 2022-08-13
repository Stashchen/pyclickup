import json
import pytest

from pyclickup import ClickUpList
from pyclickup.custom_fields import *


@pytest.fixture
def client_list_1():

    class ClientListOne(ClickUpList):
        LIST_ID = "client_1_list_id"

        short_text = ShortTextField(field_name="Short Text")
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
    with open("tests/client_raw_task_1.json") as f:
        yield json.loads(f.read())
