from datetime import datetime, timedelta
from typing import Optional

from .base import CustomField
from ..utils.validators import DateValidator
from ..utils.types import RawCustomField


class DateField(CustomField):
    TYPE = "date"
    VALIDATOR = DateValidator

    @classmethod
    def __clickup_timestamp_to_datetime(cls, timestamp: str) -> datetime:
        tmp = float(timestamp) / 1000
        return datetime.fromtimestamp(tmp)

    @classmethod
    def __datetime_to_clickup_timestamp(cls, date: datetime) -> str:
        return str(datetime.timestamp(date) * 1000) 

    def get_value(self, raw_field: RawCustomField) -> Optional[datetime]:
        timestamp = raw_field.get("value")

        if timestamp is None:
            return

        return self.__clickup_timestamp_to_datetime(timestamp)       

    def set_value(self, value: datetime, raw_field: RawCustomField) -> None:
        raw_field['value'] = self.__datetime_to_clickup_timestamp(value)
