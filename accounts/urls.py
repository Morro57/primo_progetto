from django.urls import path
from .views import signup,include

urlpatterns = [
    path('signup/',signup,name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),

]
