from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            #form.save()
            user= form.save()
            login(request,user)
            return redirect('login')
        
    else:
        form = SignUpForm()

    return render(request,'registration/signup.html',{'form':form})

