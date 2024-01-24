import requests
import config
from twilio.rest import Client

API_KEY = config.API_KEY
END_POINT = 'https://api.openweathermap.org/data/2.5/forecast'
ACCOUNT_SID = config.TWILIO_ACCOUNT_SID
AUTH_TOKEN = config.TWILIO_AUTH_TOKEN

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
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Pack your umbrella ☂️",
        to=f'whatsapp:{config.WHATSAPP_NUMBER}'
    )

