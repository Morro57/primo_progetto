from django.urls import path
from .views import home, articoloDetailView,listaArticoli,queryBase

app_name = 'news'

urlpatterns = [
    path('',home,name="homeview"),
    path("articolo/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articolo/<int:pk>",listaArticoli,name="lista_articolo_giornalista"),
    path("lista_articolo", listaArticoli, name="lista_articolo"),
    path("query" , queryBase ,name = "query_base")
]


