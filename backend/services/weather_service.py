"""
services/weather_service.py — Fetches current weather via OpenWeatherMap.
Free tier signup: https://openweathermap.org/api
"""

import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> str:
    try:
        response = requests.get(
            BASE_URL,
            params={"q": city, "appid": API_KEY, "units": "metric"},
            timeout=5,
        )
        data = response.json()

        if response.status_code != 200:
            return f"Couldn't find weather for '{city}'. Try a different city name."

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        return f"It's currently {temp}°C in {city} ({description}), feels like {feels_like}°C."

    except Exception as e:
        return f"Weather service is unavailable right now: {str(e)}"