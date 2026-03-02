from django.contrib import admin
from django.urls import path,include
from primo_progetto.views import index_root

urlpatterns = [
    path('',index_root),
    path('admin/', admin.site.urls),
    path('prima_app/',include("prima_app.urls",namespace = "prima_app")),
    path('seconda_app/',include("seconda_app.urls",namespace="seconda_app")),
    path('prova_pratica_2/',include("prova_pratica_2.urls",namespace="prova_pratica_2")),
    path('news/',include("news.urls",namespace="news")),
    path('voti/',include("voti.urls",namespace="voti")),
]
