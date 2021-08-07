from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Bikes

@admin.register(Bikes)
class BikesAdmin(ModelAdmin):
    list_display = ('bike_number', 'longitude', 'latitude','last_ride')