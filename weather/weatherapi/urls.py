from django.contrib import admin
from django.urls import path
from weatherapi.views import *

weather_list = WeatherViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('weather/', weather_list, name='weather'),
]