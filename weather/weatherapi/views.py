import datetime

from rest_framework import status
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from django.conf import settings

from weatherapi.models import *
from weatherapi.serializers import *
from weatherapi.parsers.weather_parsers import GismeteoWeather

class WeatherViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        location=self.request.query_params.get("location", "weather-kyiv-4944")
        try:
            day=int(self.request.query_params.get("day", 3))
        except ValueError:
            day=3
        
        return Weather.objects.filter(date__gte=datetime.date.today(), location=location).order_by('date')[:day]

    @method_decorator(cache_page(settings.CACHE_TIME))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        location=self.request.query_params.get("location", "weather-kyiv-4944")
        try:
            day=int(self.request.query_params.get("day", 3))
        except ValueError:
            day=3

        weather_data = GismeteoWeather(location=location, days=day)
        data = weather_data.get_weather()
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            for item in data:
                obj, created = Weather.objects.update_or_create(
                    date=item.get("date"), location=item.get("location"),
                    defaults=item,
                    )
                    
        queryset = self.get_queryset()
        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)
    

    serializer_class = WeatherSerializer