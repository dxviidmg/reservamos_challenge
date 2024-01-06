from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_places_reservamos, get_weather_data, process_weather_data


class Search(APIView):
    def get(self, request):
        places = request.GET.get("places")
        places_reservamos = get_places_reservamos(places)

        r = []
        for place in places_reservamos:
            lat = place["lat"]
            long = place["long"]
            if not lat or place["result_type"] != "city":
                continue

            name = ", ".join([place["city_name"], place["state"], place["country"]])

            weather_data = get_weather_data(lat, long)
            weather_data = process_weather_data(weather_data)

            r.append({"name": name, "weather_data": weather_data})

        return Response(r, status=status.HTTP_200_OK)
