import requests
from django.shortcuts import render

def todos_view(request):
    #lista_todos=[]
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')
        if response.status_code == 200:
            lista_todos = response.json()
            print(lista_todos)
            messaggio_errore = None
        else:
            lista_todos = []
            messaggio_errore ="Errore nel recupero dei dati. Codice d istato: " + str(response.status_code)
    except Exception as e:
        lista_todos = []
        messaggio_errore="Errore nella connessione API: "+ str(e)

    return render(request, 'todos.html',{
        'todos' : lista_todos,
        'errore' : messaggio_errore
    })
        

# Create your views here.
