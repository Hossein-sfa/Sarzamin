from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *



def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', context={'error': 'Invalid username or password'})
    return render(request, 'login.html', context={})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, 'register.html', context={'error': 'Passwords dont match'})
        elif  User.objects.filter(username=username).exists():
            return render(request, 'register.html', context={'error': 'This username exists'})
        user = User.objects.create(username=username, password=password, email= email)
        login(request, user)
        return redirect('/')
    return render(request, 'register.html', context={})
    

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
