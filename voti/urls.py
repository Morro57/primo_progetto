from django.urls import path
from .views import index,materie

app_name = 'voti'

urlpatterns = [
    path("",index,name="index_voti"),
    path("materie/",materie,name="materie")
]
