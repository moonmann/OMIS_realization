from modules import *


class NavigationMediator(abc.ABC):
    @abc.abstractmethod
    def notify(self, button):
        pass


class NavigationController(NavigationMediator):
    def __init__(self):
        self.__forecast_for_n_days_show_button = ForecastForNDaysShowButton()
        self.__search_forecast_show_button = SearchForecastViewShowButton()
        self.__current_weather_view_show_button = CurrentWeatherViewShowButton()
        self.__view_mediator = 0

    def notify(self, button):
        pass

    def react_on_forecast_for_n_days_show_button(self):
        pass

    def react_on_search_forecast_show_button(self):
        pass

    def react_on_current_weather_view_show_button(self):
        pass
