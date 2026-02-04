import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str):
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    return {
        "city": city,
        "temperature_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }
