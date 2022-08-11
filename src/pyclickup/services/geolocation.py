from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError


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
            raise Exception(
                "Something happen with Geopy request."
                "Please, check that address is valid."
            )

        if not raw_location:
            raise Exception("Address not found") 

        return Location(
            address=address,
            latitude=raw_location.latitude,
            longitude=raw_location.longitude
        )
