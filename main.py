# Some client usage
from list import ClickUpList
from custom_fields import *


class GuestTesting(ClickUpList):
    LIST_ID = 187234967

    first_name = ShortTextField(field_name="First Name") 
    last_name = ShortTextField(field_name="Last Name") 

class GuestInboundTesting(ClickUpList):
    LIST_ID = 187213511

    checkin = DateField(field_name="Checkin")
    guest_stage = DropDownField(field_name="Guest Stage")
    phone = PhoneField(field_name="Phone")
    first_name = ShortTextField(field_name="First Name")

    guests = RelationField(GuestTesting, field_name="Guests (Testing)")


if __name__ == "__main__":
    from datetime import timedelta
    task = GuestInboundTesting.get(task_id="2deuyuz")


