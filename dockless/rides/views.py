from django.shortcuts import render
from .models import Bikes
from django.contrib.auth.models import User


def end_ride(request):


    bike_record = Bikes.objects.get(user=request.user)


    if bike_record.helmet_in:
        bike_record.user = User.objects.get(username='null')

        return True
    else:
        return render(request, 'rides/invalEndRide.html') 

