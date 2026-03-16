from django.shortcuts import render
import datetime

voti={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def index(request):
    return render(request,'voti/index_voti.html')

def materie(request):
    materie=['Matematica',"Italiano","Inglese","Storia","Geografia"]
    context={
        'materie': materie
    }
    return render(request,"voti/materie.html",context)

def pagelle(request):    
    context={
        'voti': voti
    }
   
    return render(request,"voti/lista_voti.html",context)

def media(request):
    
    listaMedie=[]   

    for nome, pagella in voti.items():
        sommaVoti=0
        cont = 0
        for materia,voto,assenze in pagella:
            sommaVoti+=voto
            cont+=1
        mediaVoti=sommaVoti/cont
        listaMedie.append((nome,mediaVoti))
        
    
    

    context={
        'listaMedie' : listaMedie
        }
    return render(request,"voti/lista_media.html",context)

def max_min(request):
    materiaMin="n/d"
    nomeMin="n/d"
    votoMin=1000
    votoMax=0
    materiaMax="n/d"
    nomeMax="n/d"
    listaMin=[]
    listaMax=[]

    for nome,pagella in voti.items():
        for materia,voto,assenze in pagella:
            if(voto < votoMin):
                votoMin= voto
                nomeMin=nome
                materiaMin=materia
            if (voto >votoMax):
                votoMax= voto
                nomeMax=nome
                materiaMax=materia

    listaMin.append((nomeMin,votoMin,materiaMin))
    listaMax.append((nomeMax,votoMax,materiaMax))
    context={
        'listaMin':listaMin,
        'listaMax': listaMax
    }

    return render(request,"voti/lista_max_min.html",context)


    