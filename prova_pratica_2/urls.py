from django.urls import path
from prova_pratica_2.views import *

app_name = "prova_pratica_2"

urlpatterns = [
    path('',index,name="index"),
    path('media',media,name="media"),
    path("stringhe",stringhe,name="stringhe")
]