from modules import *
import DayForecast
import Location


class WeatherService(abc.ABC):
    @abc.abstractmethod
    def forecast_for_today(self, location):
        pass

    @abc.abstractmethod
    def forecast_for_10days(self, location):
        pass


class WeatherServiceImpl(WeatherService):
    def __init__(self):
        self.__bigDataService = 0

    def __predict_forecast(self, day_forecast_list):
        return day_forecast_list

    def forecast_for_today(self, location):
        day_forecast = 0
        return day_forecast

    def forecast_for_10days(self, location):
        day_forecast_list = 0
        return day_forecast_list
