import modules
from modules import *


class Location:
    def __init__(self, city="Minsk"):
        self.__city = city
        self.__nearest_point = ""
        self.__latitude = 0.0
        self.__longitude = 0.0
        try:
            res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                               params={'q': city, 'units': 'metric', 'APPID': modules.appid})
            data = res.json()
            self.__latitude = data['coord']['lat']
            self.__longitude = data['coord']['lon']
        except Exception as e:
            print("Exception in get location:", e)
            pass

    @property
    def city(self):
        return self.__city
