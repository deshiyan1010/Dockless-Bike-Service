import socket
import json
import os
import threading

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dockless.settings")

import django
django.setup()

from django.core.management import call_command


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.43.229', 8084))

from rides.models import Bikes
from django.contrib.auth.models import User

# def check_in_danger():
#     client.connect(('192.168.219.229', 8080))
#     # client.send(bytes("100",'utf-8'))
#     while True:
#         from_server = client.recv(4096)
#         if not from_server:
#             continue
#         if json.loads(from_server)['in_danger']==True:
#             update(json.loads(from_server))
    
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
        # bike_obj.user = User.objects.get(username='null')
        bike_obj.save()
    except:
        bike_obj = Bikes(bike_number=lp,
                        longitude=longitude,
                        latitude=latitude,
                        helmet_in=helmet_in,
                        in_danger=in_danger,
                        being_used=start,
                        user=User.objects.get(username='null')
                        )
        bike_obj.save()


def get_stat():
    global client
    client.send(bytes("100",'utf-8'))
    while True:
        from_server = client.recv(4096)
        if not from_server:
            continue     
        return json.loads(from_server)


# t1 = threading.Thread(target=check_in_danger, args=())
# t1.start()


if __name__=="__main__":
    i=0
    while 1:
        print(f"\rServer doing server shit {i}",end='')
        data = get_stat()
        update(data,True)
        print(data)
        i+=1
    client.close()