from django.shortcuts import render
from django.conf import settings
import requests
import datetime

WEATHER_ICON_MAP = {
    "Clear": "clear.png",
    "Clouds": "clouds.png",
    "Rain": "rain.png",
    "Drizzle": "drizzle.png",
    "Snow": "snow.png",
    "Thunderstorm": "thunderstorm.png",
    "Mist": "atmosphere.png",
    "Haze": "atmosphere.png",
    "Fog": "atmosphere.png",
    "Smoke": "atmosphere.png",
    "Dust": "atmosphere.png",
    "Sand": "atmosphere.png",
    "Ash": "atmosphere.png",
    "Squall": "atmosphere.png",
    "Tornado": "atmosphere.png",
}

def home(request):

    if request.method != "POST":
        return render(request, "index.html", {
            "initial": True
        })

    city = request.POST.get("city")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": settings.WEATHER_API_KEY,
        "units": "metric",
    }

    data = requests.get(url, params=params).json()

    if data.get("cod") != 200:
        return render(request, "index.html", {
            "error": True
        })

    weather_main = data["weather"][0]["main"]
    icon = WEATHER_ICON_MAP.get(weather_main, "clear.png")

    context = {
        "city": city.title(),
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": icon,
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "day": datetime.date.today(),
    }

    return render(request, "index.html", context)
