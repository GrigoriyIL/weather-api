from rest_framework import serializers

from weatherapi.models import *

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'location', 'weather', 'date', 'temperature', 'weather_feel', 'parse_date']