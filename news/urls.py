from django.urls import path
from .views import index,home, articoloDetailView,listaArticoli,queryBase,giornalistaDetailView

app_name = 'news'

urlpatterns = [
    path('',index,name="index"),
    path('homeview/',home,name="homeview"),
    path("articolo/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articolo/<int:pk>",listaArticoli,name="lista_articolo_giornalista"),
    path("lista_articolo/", listaArticoli, name="lista_articolo"),
    path("query/" , queryBase ,name = "query_base"),
    path("giornalista/<int:pk>",giornalistaDetailView,name="giornalista_detail")
]


