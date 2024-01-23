import requests
from pprint import pprint

API_KEY = '9a9a95c7c3286a35878b56c012730c2d'
END_POINT = 'https://api.openweathermap.org/data/2.5/forecast'

parameters = {
    'lat': 4.889458,
    'lon': 101.968046,
    'appid': API_KEY,
    'cnt': 6,
    'units': 'metric',
}

response = requests.get(url=END_POINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = [hourly_data.get('weather')[0].get('id') for hourly_data in weather_data.get('list')]

will_rain = False
for id in weather_id:
    if id < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella')
