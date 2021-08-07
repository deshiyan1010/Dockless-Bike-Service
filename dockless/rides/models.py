from django.db import models
from django.contrib.auth.models import User
class Bikes(models.Model):
    bike_number = models.CharField(max_length=30,primary_key=True)
    last_ride = models.TimeField(auto_now=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    helmet_in = models.BooleanField()
    in_danger = models.BooleanField()
    being_used = models.BooleanField()
    person = models.ForeignKey(User,on_delete=models.CASCADE)