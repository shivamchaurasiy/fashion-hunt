from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import Sign_up
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout

def sign_up(req):
    if req.method=="POST":
        fm = Sign_up(req.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Sign_up() 
    return render(req, 'signup.html', {'fm':fm})


def log_in(req):
    if req.method=="POST":
        fm = AuthenticationForm(request=req, data=req.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            un=fm.cleaned_data['username']  
            ps=fm.cleaned_data['password']  
            user=authenticate(username=un, password=ps)
            if user is not None:
                login(req, user)
                return redirect('/audition/')
                
    else:
        fm = AuthenticationForm()
    return render(req, 'login.html', {'fm':fm})

def log_out(req):
    logout(req) 
    return HttpResponseRedirect("/login/") 


def profile(req):
    if req.user.is_authenticated:
        return render(req, 'header.html', {'name':req.user})
    else:
        return HttpResponseRedirect("/login/")   