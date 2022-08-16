import pytest
from datetime import datetime

from pyclickup.services.geolocation import Location
from pyclickup.utils.exceptions.validators import ValidationError
from pyclickup.utils.exceptions.fields import RequiredFieldMissing


# Required field
def test_non_required_field__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.text is None

def test_required_field__set_none__raise_error(client_1_task):
    with pytest.raises(RequiredFieldMissing):
        client_1_task.short_text = None

# Text field
def test_text_field_get__exists__return_string(client_1_task):
    assert client_1_task.text == "Some text"

def test_text_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.text is None
    
def test_text_field_set__string_value__update_field(client_1_task):
    client_1_task.text = "New text"
    assert client_1_task.text == "New text"

def test_text_field_set__not_string_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.text = 123

# Short Text field
def test_short_text_field_get__exists__return_string(client_1_task):
    assert client_1_task.short_text == "Some text"

def test_short_text_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.short_text is None
    
def test_short_text_field_set__string_value__update_field(client_1_task):
    client_1_task.short_text = "New text"
    assert client_1_task.short_text == "New text"

def test_short_text_field_set__not_string_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.short_text = 123

# Url field
def test_url_field_get__exists__return_string(client_1_task):
    assert client_1_task.link == "https://some_url"

def test_url_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.link is None
    
def test_url_field_set__string_value__update_field(client_1_task):
    client_1_task.link = "https://some_url"
    assert client_1_task.link == "https://some_url"

def test_url_field_set__not_string_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.link = "simple_string"

# Email field
def test_email_field_get__exists__return_string(client_1_task):
    assert client_1_task.email == "example@example.com"

def test_email_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.email is None
    
def test_email_field_set__string_value__update_field(client_1_task):
    client_1_task.email = "test@example.com"
    assert client_1_task.email == "test@example.com"

def test_email_field_set__not_string_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.email = "simple_string"

# Drop Down field
def test_drop_down_field_get__exists__return_string(client_1_task):
    assert client_1_task.drop_down == "Option 1"

def test_drop_down_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.drop_down is None
    
def test_drop_down_field_set__valid_option__update_field(client_1_task):
    client_1_task.drop_down = "Option 2"
    assert client_1_task.drop_down == "Option 2"

def test_drop_down_field_set__not_valid_option__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.drop_down = "invalid_option"

# Relations field
def test_relation_field_get__exists__return_list_of_tasks(
    monkeypatch, client_list_2, client_1_task, raw_task_for_client_2
):
    monkeypatch.setattr(
        "pyclickup.custom_fields.relation.clickup_api.get_task",
        lambda task_id: raw_task_for_client_2
    )

    assert isinstance(client_1_task.clients_2, list)
    assert len(client_1_task.clients_2) == 1

    good_task = client_1_task.clients_2[0]

    assert isinstance(good_task, client_list_2)
    assert good_task.id == "client_2_task_id"

def test_relation_field_get__no_data__return_empty_list(client_1_empty_task):
    assert client_1_empty_task.clients_2 == []

def test_relation_field_set__valid_task__update_field(
    monkeypatch, client_1_task, client_2_task, raw_task_for_client_2
):
    raw_task_for_client_2['id'] = "some_good_id"

    monkeypatch.setattr(
        "pyclickup.custom_fields.relation.clickup_api.get_task",
        lambda task_id: raw_task_for_client_2
    )

    assert len(client_1_task.clients_2) == 1
    client_1_task.clients_2 = client_2_task
    assert len(client_1_task.clients_2) == 2

def test_relation_field_set__not_task__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.clients_2 = 123

# Phone field
def test_phone_field_get__exists__return_string(client_1_task):
    assert client_1_task.phone == "+9417023418"

def test_phone_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.phone is None

def test_phone_field_set__valid_string__update_field(client_1_task):
    client_1_task.phone = "+1234567890"
    assert client_1_task.phone == "+1234567890"

    client_1_task.phone = "+123 456 7890"
    assert client_1_task.phone == "+123 456 7890"

def test_phone_field_set__invalid_string__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.phone = "Invalid string"

# Checkbox field
def test_checkbox_field_get__exists__return_bool(client_1_task):
    assert client_1_task.checkbox == True

def test_checkbox_field_get__no_data__return_false(client_1_empty_task):
    assert client_1_empty_task.checkbox is False

def test_checkbox_field_set__bool__update_field(client_1_task):
    client_1_task.checkbox = False
    assert client_1_task.checkbox == False

def test_checkbox_field_set__not_bool__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.checkbox = "Some string"

# Number field
def test_number_field_get__exists__return_int_or_float(client_1_task):
    assert client_1_task.number == 123 

def test_number_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.number is None    

def test_number_field_set__number_value__update_field(client_1_task):
    client_1_task.number = 321
    assert client_1_task.number == 321
    client_1_task.number = 321.12
    assert client_1_task.number == 321.12

def test_number_field_set__not_number_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.number = "Invalid number data" 

# Currency field
def test_currency_field_get__exists__return_float(client_1_task):
    assert client_1_task.currency == 500.0 

def test_currency_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.currency is None    

def test_currency_field_set__number_value__update_field(client_1_task):
    client_1_task.currency = 321
    assert client_1_task.currency == 321
    client_1_task.currency = 321.12
    assert client_1_task.currency == 321.12

def test_currency_field_set__not_number_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.currency = "Invalid number data" 

# Location field
def test_location_field_get__exists__return_address_as_string(client_1_task):
    assert client_1_task.location == "221B Baker St"

def test_location_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.location is None

def test_location_field_set__string__update_field(
    monkeypatch, client_1_task
):
    monkeypatch.setattr(
        "pyclickup.custom_fields.location.geo_grabber.search",
        lambda address: Location(latitude=12.12,
                                 longitude=21.21,
                                 address="11 Fake Hills")
    )

    client_1_task.location = "11 Fake Hills"
    assert client_1_task.location == "11 Fake Hills"    

def test_location_field_set__not_string__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.location = 123

# Date field
def test_date_field_get__exists__return_datetime(client_1_task):
    assert client_1_task.date == datetime(2022, 12, 12, 0, 0)

def test_date_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.date is None

def test_date_field_set__datetime__update_field(client_1_task):
    client_1_task.date = datetime(2022, 11, 11)
    assert client_1_task.date == datetime(2022, 11, 11)

def test_date_field_set__not_datetime__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.date = 13

# Labels field
def test_labels_field_get__exists__return_list_of_labels(client_1_task):
    assert client_1_task.labels == ["Label #1"]

def test_labels_field_get__no_data__return_empty_list(client_1_empty_task):
    assert client_1_empty_task.labels == []

def test_labels_field_set__good_option__upadate_field(client_1_task):
    client_1_task.labels = "Label #2"
    assert client_1_task.labels == ["Label #1", "Label #2"]

    client_1_task.labels = None
    assert client_1_task.labels == []

    client_1_task.labels = ["Label #1", "Label #2"]
    assert client_1_task.labels == ["Label #1", "Label #2"]

def test_labels_field_set__invalid_option__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.labels = 123

# Formula field
def test_formula_field_get__exists__return_string(client_1_task):
    assert client_1_task.formula == "From Formula"

def test_formula_field_get__no_data__return_none(client_1_empty_task):
    assert client_1_empty_task.formula is None

def test_formula_field_set__any_value__raise_error(client_1_task):
    with pytest.raises(ValidationError):
        client_1_task.formula = "Some data"
    
