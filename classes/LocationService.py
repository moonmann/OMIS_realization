from modules import *
from classes.Singleton import singleton


@singleton
class LocationService(abc.ABC):

    def get_curr_location(self):
        location = geocoder.ip('me')
        my_location = Location(city=location.city)
        return my_location

    def get_location_by_name(self, name):
        my_location = Location(city=name)
        return my_location
