from django.urls import path                                                                                                                          
from . import views

app_name = "maps"

urlpatterns = [ 
    path("map/", views.map, name="map"),
]
