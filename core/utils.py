import requests
from datetime import datetime
from django.conf import settings

def get_places_reservamos(query):
    url = "{}/places?q={}".format(settings.RESERVAMOS_API, query)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a Reservamos API: {e}")
        return []

def get_weather_data(lat, long):
    url = "{}?lat={}&lon={}&exclude=current,minutely,hourly&appid={}".format(
        settings.OPEN_WEATHER_API, lat, long, settings.OPEN_WEATHER_API_KEY
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a OpenWeather API: {e}")
        return {}

def process_weather_data(data):
    if "daily" not in data:
        print("Error: Datos diarios no encontrados en la respuesta.")
        return []

    result = []
    for data_daily in data["daily"]:
        date = datetime.utcfromtimestamp(data_daily["dt"])
        temp = data_daily["temp"]
        result.append({"date": date, "temp_max": temp["max"], "temp_min": temp["min"]})
    return result
