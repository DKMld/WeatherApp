from django.contrib import admin
from django.urls import path, include
from WeatherApp.weather import urls as weather_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(weather_urls)),
]
