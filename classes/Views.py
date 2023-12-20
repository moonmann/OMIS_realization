from modules import *
from classes.UserController import UserController
from classes.LocationService import LocationService


class ForecastForNDaysView(abc.ABC):
    def __init__(self):
        self.__user_controller = UserController()

    def show_forecast_for_n_days(self):
        return self.__user_controller.get_location()


class SearchForecastView(abc.ABC):
    def __init__(self):
        self.__location_service = LocationService()

    def show_search_dialog(self):
        pass


class CurrentWeatherView(abc.ABC):
    def __init__(self):
        self.__user_controller = UserController()

    def show_current_weather(self):
        return self.__user_controller.get_location()
