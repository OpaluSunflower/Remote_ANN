from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello world!")

def test(request):
    return render(request,'base.html')    
# Create your views here.

def home(request):
    if(request.user.is_authenticated):
        return HttpResponse("Witaj" + request.user.username)
    else:
        return HttpResponse("Zaloguj się!")

def register(request):
    if request.method == "POST":    
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            email = request.POST["email"]
            password = request.POST["password"]
            user,created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password)
                user.save()
                return redirect('/Aplikacja/signIn')
            else:
                messages.warning(request,"Użytkownaik istnieje w bazie")    
    if not request.user.is_authenticated:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    else:
        return redirect('/Aplikacja/signIn')    

def signIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            password = request.POST["password"]
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Zalogowano pomyślnie")
            else:
                messages.warning(request,"Źle")
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        form = LoginForm()
        return render(request,'signIn.html',{'form':form})    
