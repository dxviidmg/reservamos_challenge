import requests
from datetime import datetime

def get_places_reservamos(query):
    url = f"https://search.reservamos.mx/api/v2/places?q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a Reservamos API: {e}")
        return []

def get_weather_data(lat, long):
    api_key = "a5a47c18197737e8eeca634cd6acb581"
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&exclude=current,minutely,hourly&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(type(response.json()))
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
