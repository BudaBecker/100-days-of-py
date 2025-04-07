import requests
import os
from dotenv import load_dotenv

load_dotenv(".venv/.env")
weather_api_key = os.getenv("WeatherAPI")
my_lat = os.getenv("MyLAT")
my_lon = os.getenv("MyLONG")

params = {
    "lat": float(my_lat),
    "lon": float(my_lon),
    "appid": weather_api_key,
    "units": "metric"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params)
response.raise_for_status()
weather_data = response.json()
print (
    f"Weather Main: {weather_data["weather"][0]["main"]}\n"
    f"Weather desc: {weather_data["weather"][0]["description"]}\n"
    f"Temp: {weather_data["main"]["temp"]}°C, feels like {weather_data["main"]["feels_like"]}°C"
)