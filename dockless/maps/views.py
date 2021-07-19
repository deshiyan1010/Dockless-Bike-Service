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

    for coords in staticdb.QR_LOCATIONS:
        folium.Marker(location=tuple(coords),tooltip='QR Code',icon=folium.Icon(color='green')).add_to(m)
    m = m._repr_html_()
    return render(request, 'maps/default.html', 
                  { 'map': m })

