from modules import *
from ViewController import app, ViewController, ViewType


class Injector:
    def __init__(self):
        self.__view_controller = ViewController()

    def run(self, view_type, city=""):
        return self.__view_controller.notify(view_type=view_type, city=city)


i = Injector()


@app.get("/")
def read_root():
    return i.run(ViewType.CURRENT_WEATHER)


@app.get("/forecast")
def read_root():
    return i.run(ViewType.FORECAST_FOR_TODAY)


@app.get("/search")
def read_root(city: str):
    return i.run(ViewType.SEARCH, city)


@app.get("/search_for_5_days")
def read_root(city: str):
    return i.run(ViewType.SEARCH_FOR_5_DAYS, city)


@app.get("/5_days")
def read_root():
    return i.run(ViewType.FORECAST_FOR_N_DAYS)


@app.get("/forecast_5_days")
def read_root():
    return i.run(ViewType.FORECAST_FOR_5_DAYS)


uvicorn.run(app, host="127.0.0.1", port=8000)
