import requests
from datetime import datetime


def get_places_reservamos(places):
    url = "https://search.reservamos.mx/api/v2/places?q=" + places
    response = requests.request("GET", url)
    return response.json()

def get_weather_data(lat, long):
    api_key = "a5a47c18197737e8eeca634cd6acb581"
    
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat+ "&lon=" + long +"&exclude=current,minutely,hourly&appid=" + api_key
    response = requests.request("GET", url)
    return response.json()

def process_weather_data(data):
    result = []
    for data_daily in data['daily']:
        date = datetime.utcfromtimestamp(data_daily['dt'])
        temp = data_daily['temp']
        result.append({
            'date': date,
            'temp_max': temp['max'],
            'temp_min': temp['min']
        })
    return result