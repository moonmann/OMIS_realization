import abc
import requests
import enum
import datetime
import geocoder
from fastapi import FastAPI, Response, Query, Body, Depends, Request, Form
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from classes.Buttons import ForecastForNDaysShowButton, SearchForecastViewShowButton,CurrentWeatherViewShowButton
from classes.Navigator import NavigationMediator
from classes.Location import Location
from classes.Navigator import NavigationController
appid = "67d2c1364070059bafacb61698b4ae13"
