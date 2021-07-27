from django.shortcuts import render
import folium
import geocoder
from . import staticdb
from django.core.files.storage import FileSystemStorage
from dockless.settings import BASE_DIR
from qr.views import valQR
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import math

def euc(c1,c2):
    return math.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)


def default_map(request):


    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        val = valQR(os.getcwd()+str(uploaded_file_url))
        if val==1:
            return HttpResponseRedirect(reverse('rewards:valReward'))
        else:
            return HttpResponseRedirect(reverse('rewards:invalReward'))

            
    g = geocoder.ip('me')
    m = folium.Map(height=800,width=1000,location=tuple(g.latlng))
    folium.Marker(location=tuple(g.latlng),tooltip='You are here.',icon=folium.Icon(color='red')).add_to(m)
    print(g.latlng)
    min = euc(g.latlng,staticdb.QR_LOCATIONS[0])
    mincord = staticdb.QR_LOCATIONS[0]
    for coords in staticdb.QR_LOCATIONS[1:]:
        if euc(g.latlng,coords)<min:
            min = euc(g.latlng,coords)
            mincord = coords
    for coords in staticdb.QR_LOCATIONS:
        if mincord==coords:
            folium.Marker(location=tuple(coords),tooltip='QR Code',icon=folium.Icon(color='blue')).add_to(m)
        else:
            folium.Marker(location=tuple(coords),tooltip='QR Code',icon=folium.Icon(color='green')).add_to(m)
    m = m._repr_html_()
    return render(request, 'maps/default.html', 
                  { 'map': m })

