import math
from django.shortcuts import render, redirect
import requests


def home_page(request):

    user_current_location = get_user_location()
    weather_data = get_weather_data(request, user_current_location['city'])

    context = {
        'temp': math.ceil(weather_data['main']['temp']),
        'description': weather_data['weather'][0]['main'],
        'city': user_current_location['city'],
    }

    return render(request, 'home_page.html', context)


def get_info_from_search(request):

    if request.method == 'GET':
        city_input = request.GET.get('city_input')
        weather_data = get_weather_data(request, city_input)

        if len(city_input) > 0:
            context = {
                'temp': math.ceil(weather_data['main']['temp']),
                'description': weather_data['weather'][0]['main'],
                'city': city_input,
            }
            return render(request, 'home_page.html', context)

        return redirect('home_page')


def get_weather_data(request, city):
    api_key = 'd9cfcf4247b97e74578bb2a0f9e6cedf'

    api_request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(api_request)

    data = response.json()

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

    return location_data
