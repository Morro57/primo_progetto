from django.shortcuts import render
import datetime

def index(request):
    return render(request,'voti/index_voti.html')

def materie(request):
    materie=['Matematica',"Italiano","Inglese","Storia","Geografia"]
    context={
        'materie': materie
    }
    return render(request,"voti/materie.html",context)

def pagelle(request):
    voti={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    context={
        'voti': voti
    }
   
    return render(request,"voti/lista_voti.html",context)

def media(request):

    return render(request)

def max_min(request):

    return render(request)


    