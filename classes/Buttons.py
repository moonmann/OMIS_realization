from modules import *


class BaseButton:
    def __init__(self):
        self._mediator = NavigationMediator()


class ForecastForNDaysShowButton(abc.ABC):
    def show(self):
        pass


class SearchForecastViewShowButton(abc.ABC):
    def show(self):
        pass


class CurrentWeatherViewShowButton(abc.ABC):
    def show(self):
        pass
