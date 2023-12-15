from modules import *


class Location:
    def __init__(self, city):
        self.__city = city
        self.__latitude = 0
        self.__longitude = 0

    @property
    def city(self):
        return self.__city
