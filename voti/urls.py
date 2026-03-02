from django.urls import path
from .views import index,materie,pagelle,media,max_min

app_name = 'voti'

urlpatterns = [
    path("",index,name="index_voti"),
    path("materie/",materie,name="materie"),
    path("lista_voti/",pagelle,name="lista_voti"),
    path("media_voti/",media,name="media_voti"),
    path("lista_max_min/",max_min,name="lista_max_min")
]
