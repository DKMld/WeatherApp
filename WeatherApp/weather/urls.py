from django.contrib import admin
from django.urls import path

from WeatherApp.weather import views as weather_views

urlpatterns = [
    path('', weather_views.home_page, name='home_page'),
    path('search', weather_views.get_info_from_search, name='search'),
]
