from django.urls import path
from . import views

app_name = "rewards"

urlpatterns = [
    path('valReward/',views.valReward,name='valReward'),
    path('invalReward/',views.invalReward,name='invalReward'),

]
