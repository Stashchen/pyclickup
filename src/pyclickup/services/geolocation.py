from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

from ..utils.exceptions.geolocation import AddressNotFound


@dataclass
class Location:
    latitude: float
    longitude: float
    address: str

    def to_dict(self) -> dict:
        """Return same dict structure as ClickUp provide for Location Field"""
        return dict(
            location=dict(lat=self.latitude,
                          lng=self.longitude),
            formatted_address=self.address
        )

class GeolocationGrabber:
    """
    Service that will find out the details about specific address,
    using geopy library.
    """

    def __init__(self):
        self._geolocator = Nominatim(user_agent=self.__class__.__name__)

    def search(self, address: str) -> Location:
        try:
            raw_location = self._geolocator.geocode(address)
        except GeopyError:
            raise GeopyError(
                "Something happen with Geopy request."
                "Please, check that entered address is valid."
            )

        if not raw_location:
            raise AddressNotFound(f"`{address}` is not valid or not found.") 

        return Location(
            address=address,
            latitude=raw_location.latitude,
            longitude=raw_location.longitude
        )
