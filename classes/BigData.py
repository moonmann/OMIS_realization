from modules import *

from classes.DayForecast import DayForecast
from classes.Singleton import singleton


def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15


@singleton
class BigDataService:
    def __init__(self):
        self.__data = dict()

    def updateData(self, forecast, location: Location):
        self.__data[location].append(forecast)

    def updateData(self):
        pass

    def getData(self, location: Location):
        return self.__data[location]

    def getCurrentWeather(self, location: Location):
        res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                           params={'q': location.city, 'lang': 'ru', 'units': 'metric', 'APPID': appid})
        data = res.json()
        curr_weather = DayForecast(weather_conditions=data["weather"]["main"],
                                   wind_speed=data["wind"]["speed"],
                                   precipitation=data["weather"]["description"],
                                   temperature=data["main"]["temp"],
                                   date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return curr_weather

    def getWeatherForToday(self, location: Location):
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                           params={'q': location.city, 'lang': 'ru', 'APPID': appid})
        data = res.json()
        current_date = datetime.datetime.now().date()

        forecast_list = data['list']
        daily_forecast = [forecast for forecast in forecast_list if
                          current_date == datetime.datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S").date()]

        forecast_for_today = []
        for forecast in daily_forecast:
            curr_weather = DayForecast(weather_conditions=forecast["weather"][0]["main"],
                                       wind_speed=forecast["wind"]["speed"],
                                       precipitation=forecast['weather'][0]['description'],
                                       temperature=round(kelvin_to_celsius(forecast['main']['temp']), 1),
                                       date=forecast['dt_txt'])
            forecast_for_today.append(curr_weather)
        return forecast_for_today

    def getWeatherFor5Days(self, location: Location):
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                           params={'q': location.city, 'lang': 'ru', 'APPID': appid})
        data = res.json()

        forecast_list = data['list']

        forecast_for_10days = []
        for forecast in forecast_list:
            curr_weather = DayForecast(weather_conditions=forecast["weather"][0]["main"],
                                       wind_speed=forecast["wind"]["speed"],
                                       precipitation=forecast['weather'][0]['description'],
                                       temperature=round(kelvin_to_celsius(forecast['main']['temp']), 1),
                                       date=forecast['dt_txt'])
            forecast_for_10days.append(curr_weather)
        return forecast_for_10days
