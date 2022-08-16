from datetime import datetime
from typing import Union


class ClickupDateFormat:
    """
    This class has methods that will
    translate ClickUp's timestamps to datetime.

    ClickUp date format is: str(default timestamp * 1000)
    E.g. "604800000"
    """
    
    @staticmethod
    def timestamp_to_datetime(
        clickup_timestamp: Union[str, float, int]
    ) -> datetime:
        if type(clickup_timestamp) not in [str, float, int]:
            raise TypeError(
                "`clickup_timestamp` must be on of the following types:"
                "[str, float, int]"
            )

        return datetime.fromtimestamp(float(clickup_timestamp) / 1000)
        
    @staticmethod
    def datetime_to_timestamp(datetime_obj: datetime) -> str:
        if not isinstance(datetime_obj, datetime):
            raise TypeError("`datetime_obj` must be a `datetime` instance.")

        return str(datetime_obj.timestamp() * 1000)       
