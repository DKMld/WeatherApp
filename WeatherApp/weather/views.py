import math

from django.shortcuts import render
import requests
import json


def home_page(request):

    if request.method == 'POST':
        city_input = request.POST.get('city_input')
        weather_data = get_weather_data(request, city_input)

        context = {
            'temp': math.ceil(weather_data['main']['temp']),
            'description': weather_data['weather'][0]['main'],
            'city': city_input,

        }
        return render(request, 'home_page.html', context)

    user_current_location = get_user_location()
    weather_data = get_weather_data(request, user_current_location['city'])
    context = {
        'temp': math.ceil(weather_data['main']['temp']),
        'description': weather_data['weather'][0]['main'],
        'city': user_current_location['city'],
    }

    return render(request, 'home_page.html', context)


def get_weather_data(request, city):
    api_key = 'd9cfcf4247b97e74578bb2a0f9e6cedf'

    api_request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(api_request)

    data = response.json()
    print(data)
    return data





def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_user_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    print(location_data)
    return location_data



