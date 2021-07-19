from django.conf.urls import url                                                                                                                              
from . import views

app_name = "maps"

urlpatterns = [ 
    url("", views.default_map, name="map"),
]
