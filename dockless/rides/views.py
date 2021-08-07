from django.shortcuts import render
import socket
from models import Bikes


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def get_stat():
    client.connect(('0.0.0.0', 8080))
    client.send(bytes("100",'utf-8'))
    while True:
        from_server = client.recv(4096)
        if not from_server:
            continue
        client.close()
        return from_server

def update(data,start):
    lp = data['lp']
    in_danger = data['in_danger']
    helmet_in = data['helmet_in']
    latitude = data['latitude']
    longitude = data['longitude']

    try:
        bike_obj = Bikes.objects.get(bike_number=lp)
        bike_obj.in_danger = in_danger
        bike_obj.helmet_in = helmet_in
        bike_obj.latitude = latitude
        bike_obj.longitude = longitude
        bike_obj.being_used = start
        bike_obj.save()
    except:
        bike_obj = Bikes(bike_number=lp,
                        longitude=longitude,
                        latitude=latitude,
                        helmet_in=helmet_in,
                        in_danger=in_danger,
                        being_used=start,
                        )
        bike_obj.save()   

def start_ride(request):
    status = get_stat()
    update(status,True)


def end_ride(request):
    status = get_stat()
    lp = status['lp']
    helmet_in = status['helmet_in']
    in_danger = status['in_danger']
    latitude = status['latitude']
    longitude = status['longitude']

    

    if helmet_in!=bytes("101",'utf-8'):
        update(status,False)

        return render(request, 'rides/valEndRide.html') 
    else:
        return render(request, 'rides/invalEndRide.html') 