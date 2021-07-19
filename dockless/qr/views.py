from django.shortcuts import render
import geocoder
from maps import staticdb
import math
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.core.files.storage import FileSystemStorage

from PIL import Image
from pyzbar.pyzbar import decode


def euc(c1,c2):
    return math.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)


def valQR(path):

    data = decode(Image.open(path))

    if data[0].data == staticdb.QR_DATA:
        g = geocoder.ip('me').latlng
        min = euc(staticdb.QR_LOCATIONS[0],g)
        for coords in staticdb.QR_LOCATIONS[1:]:
            dist = euc(coords,g)
            if dist<min:
                min = dist
        if min<0.5:
            return 1
            
        else:
            return 0

    return 0