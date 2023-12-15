from modules import *


class WeatherCondition(enum.Enum):
    SUNNY = 1
    RAINY = 2
    SNOWY = 3
    STORMY = 4


class DayForecast:
    def __init__(self, weather_conditions, wind_speed, precipitation, temperature, date):
        self.__weather_conditions = weather_conditions
        self.__wind_speed = wind_speed
        self.__precipitation = precipitation
        self.__temperature = temperature
        self.__date = date

    @property
    def weather_conditions(self):
        return self.__weather_conditions

    @property
    def wind_speed(self):
        return self.__wind_speed

    @property
    def precipitation(self):
        return self.__precipitation

    @property
    def temperature(self):
        return self.__temperature

    @property
    def date(self):
        return self.__date
