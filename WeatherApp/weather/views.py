from django.shortcuts import render
import requests
import json


def home_page(request):
    weather_data = get_weather_data(request)

    context = {'temp': weather_data['main']['temp'],
               'description': weather_data['weather'][0]['main'],
               }
    return render(request, 'home_page.html', context)


def get_weather_data(request):
    user_current_city = get_user_location()
    api_key = 'd9cfcf4247b97e74578bb2a0f9e6cedf'

    api_request = f'https://api.openweathermap.org/data/2.5/weather?q={user_current_city}&appid={api_key}&units=metric'
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
    return location_data['city']


