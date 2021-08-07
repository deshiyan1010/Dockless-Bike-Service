from django.shortcuts import render
import geocoder
from maps import staticdb
import math
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.core.files.storage import FileSystemStorage

from PIL import Image
from pyzbar.pyzbar import decode
import cv2
import pyzbar


def euc(c1,c2):
    return math.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)


def read_barcodes(frame):
    barcodes = decode(frame)
    print(frame.shape)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data
        # cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        # #2
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        # #3
        # with open("barcode_result.txt", mode ='w') as file:
        #     file.write("Recognized Barcode:" + barcode_info)
        barcode_info = barcode_info.decode('utf-8')
        print("Barcode:", barcode_info)
        return barcode_info



def valQR(path):

    # data = decode(Image.open(path))
    data = read_barcodes(cv2.imread(path,1))
    print(type(data),type(staticdb.QR_DATA))
    
    if data == staticdb.QR_DATA:

        g = geocoder.ip('me').latlng
        min = euc(staticdb.QR_LOCATIONS[0],g)
        for coords in staticdb.QR_LOCATIONS[1:]:
            dist = euc(coords,g)
            if dist<min:
                min = dist
        if min<0.4:
            return 1
            
        else:
            return 0

    return 0