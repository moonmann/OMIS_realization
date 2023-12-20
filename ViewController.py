from modules import *
from classes.WeatherService import WeatherServiceImpl
from classes.Views import *

app = FastAPI()
templates = Jinja2Templates(directory="classes/UI")


class ViewType(enum.Enum):
    CURRENT_WEATHER = 1
    FORECAST_FOR_N_DAYS = 2
    SEARCH = 3
    FORECAST_FOR_TODAY = 4
    FORECAST_FOR_5_DAYS = 5
    SEARCH_FOR_5_DAYS = 6


class ViewMediator(abc.ABC):
    @abc.abstractmethod
    def notify(self, view_type):
        pass


class ViewController(ViewMediator):
    def __init__(self):
        self.__current_weather_view = CurrentWeatherView()
        self.__forecast_for_n_days_view = ForecastForNDaysView()
        self.__search_forecast_view = SearchForecastView()
        self.__weather_service = WeatherServiceImpl()
        self.__navigation_mediator = NavigationController()

    def notify(self, view_type, city=""):
        if view_type == ViewType.CURRENT_WEATHER:
            return self.react_on_show_current_weather()

        if view_type == ViewType.FORECAST_FOR_TODAY:
            return self.react_on_show_forecast_for_today()

        if view_type == ViewType.FORECAST_FOR_N_DAYS:
            return self.react_on_show_forecast_for_n_days()

        if view_type == ViewType.SEARCH:
            return self.react_on_show_search_form(city)

        if view_type == ViewType.SEARCH_FOR_5_DAYS:
            return self.react_on_show_search_for_5_days_form(city)

        if view_type == ViewType.FORECAST_FOR_5_DAYS:
            return self.react_on_show_forecast_for_5_day()

    def react_on_show_current_weather(self):
        return FileResponse('classes/UI/main.html')

    def react_on_show_forecast_for_n_days(self):
        return FileResponse('classes/UI/5_days.html')

    def react_on_show_forecast_for_5_day(self):
        location = self.__current_weather_view.show_current_weather()
        forecast = self.__weather_service.forecast_for_5days(location=location)
        hourly_forecast = [
            {"time": f"{i.date}", "temperature": i.temperature, "wind_speed": i.wind_speed,
             "precipitation": i.precipitation}
            for i in forecast if i.date.split()[1][:2] == "12"
        ]
        rez = {
            "city": location.city,
            "hourly": hourly_forecast
        }
        return rez

    def react_on_show_forecast_for_today(self):
        location = self.__forecast_for_n_days_view.show_forecast_for_n_days()
        forecast = self.__weather_service.forecast_for_today(location=location)
        hourly_forecast = [
            {"time": f"{i.date}", "temperature": i.temperature, "wind_speed": i.wind_speed,
             "precipitation": i.precipitation}
            for i in forecast
        ]
        rez = {
            "city": location.city,
            "temperature": forecast[0].temperature,
            "wind_speed": forecast[0].wind_speed,
            "humidity": forecast[0].temperature,
            "precipitation": forecast[0].precipitation,
            "hourly": hourly_forecast
        }
        return rez

    def react_on_show_search_form(self, city):
        forecast = self.__weather_service.forecast_for_today(location=Location(city=city))
        hourly_forecast = [
            {"time": f"{i.date}", "temperature": i.temperature, "wind_speed": i.wind_speed,
             "precipitation": i.precipitation}
            for i in forecast
        ]
        rez = {
            "city": city,
            "temperature": forecast[0].temperature,
            "wind_speed": forecast[0].wind_speed,
            "humidity": forecast[0].temperature,
            "precipitation": forecast[0].precipitation,
            "hourly": hourly_forecast
        }
        return rez

    def react_on_show_search_for_5_days_form(self, city):
        forecast = self.__weather_service.forecast_for_5days(location=Location(city=city))
        hourly_forecast = [
            {"time": f"{i.date}", "temperature": i.temperature, "wind_speed": i.wind_speed,
             "precipitation": i.precipitation}
            for i in forecast if i.date.split()[1][:2] == "12"
        ]
        rez = {
            "city": city,
            "hourly": hourly_forecast
        }
        return rez
