from fastapi import FastAPI, Response, Query, Body, Depends, Request, Form
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="UI")


@app.get("/")
def main():
    return FileResponse('classes/UI/main.html')


@app.get("/forecast")
def main(city: str):
    weather_data = {
        "city": city,
        "temperature": 25,
        "wind_speed": 10,
        "humidity": 50,
        "hourly": [
            {"time": "12:00", "temperature": 27, "wind_speed": 12},
            {"time": "15:00", "temperature": 26, "wind_speed": 11},
        ]
    }

    return weather_data


uvicorn.run(app, host="127.0.0.1", port=8000)