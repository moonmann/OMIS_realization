from modules import *
from classes.Location import Location
from classes.BigData import BigDataService


class WeatherService(abc.ABC):
    @abc.abstractmethod
    def forecast_for_today(self, location):
        pass

    @abc.abstractmethod
    def forecast_for_5days(self, location):
        pass


class WeatherServiceImpl(WeatherService):
    def __init__(self):
        self.__bigDataService = BigDataService()

    def __predict_forecast(self, day_forecast_list):
        return day_forecast_list

    def forecast_for_today(self, location: Location):
        return self.__bigDataService.getWeatherForToday(location)

    def forecast_for_5days(self, location: Location):
        return self.__bigDataService.getWeatherFor5Days(location)
