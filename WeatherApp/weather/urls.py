from django.contrib import admin
from django.urls import path

from WeatherApp.weather import views as weather_views

urlpatterns = [
    path('', weather_views.home_page),
]
