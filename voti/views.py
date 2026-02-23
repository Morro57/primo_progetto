from django.shortcuts import render
import datetime
from.models import materie

def index(request):
    return render(request,"voti/index_voti.html")

def materie(request):
    materie=['Matematica',"Italiano","Inglese","Storia","Geografia"]

    return render(request,"voti/materie.html",context=materie)
