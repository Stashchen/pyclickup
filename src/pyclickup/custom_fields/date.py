from datetime import datetime
from typing import Optional

from .base import CustomField
from ..utils.date_format import ClickupDateFormat
from ..utils.validators import DateValidator
from ..utils.types import RawCustomField


class DateField(CustomField):
    TYPE = "date"
    VALIDATOR = DateValidator

    def get_value(self, raw_field: RawCustomField) -> Optional[datetime]:
        timestamp = raw_field.get("value")

        if timestamp is None:
            return

        return ClickupDateFormat.timestamp_to_datetime(timestamp)       

    def set_value(self, value: datetime, raw_field: RawCustomField) -> None:
        raw_field['value'] = ClickupDateFormat.datetime_to_timestamp(value)
