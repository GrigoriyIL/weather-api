from django.contrib import admin
from weatherapi.models import *

class WeatherAdmin(admin.ModelAdmin):
    list_display = ['location', 'date', 'weather', 'temperature', 'weather_feel','parse_date']
    list_display_links = ['location']
    readonly_fields=['location', 'date', 'weather', 'temperature', 'weather_feel','parse_date']


admin.site.register(Weather, WeatherAdmin)