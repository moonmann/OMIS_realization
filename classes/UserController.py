from modules import *
from classes.LocationService import LocationService
from classes.Singleton import singleton


@singleton
class UserController:
    def __init__(self):
        self.__location_service = LocationService()
        self.__location = self.__location_service.get_curr_location()

    def get_location(self):
        return self.__location
