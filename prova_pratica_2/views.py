from django.shortcuts import render
import random

def index(request):
    return render(request,"index3.html")

def media(request):

    n1=random.randint(1,50)
    n2=random.randint(1,50)
    n3=random.randint(1,50)

    media=(n1+n2+n3)/3

    context={
        "n1" : n1,
        "n2" : n2,
        "n3" : n3,
        "media": media
    }

    return render(request,"media.html",context)

def stringhe(request):

    lista = [("cane",4),("gatto",5),("casa",4),("auto",4), ("gioco",5),("contemporaneamente",18),("Francesco",9),("aula",4),("calcio",6),("pappagallo",10)]

    contMagg=0
    contMin=0

    for parola,lunghezza in lista:
        if(lunghezza>=5):
            contMagg+=1
        else:
            contMin+=1


    context={
        "lista" : lista,
        "contMagg" : contMagg,
        "contMin" : contMin
    }
    return render(request,"stringhe.html",context)
