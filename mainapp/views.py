from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from blogs.views import category
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from blogs.models import Article

# Create your views here.
def index(request):
    tendences = Article.objects.filter(public=True).order_by("-created_at")[:3]
    return render(request, 'mainapp/index.html', {'title':"Inicio", 'tendences': tendences})


def about(request):

    return render(request, 'mainapp/about.html', {'title':"Sobre nosotros"})

def register_page(request):
    register_form = RegisterForm()
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Te has registrado correctamente")
                return redirect('inicio')

        return render(request, 'users/register.html', {
            'title': "Registro",
            'register_form': register_form,
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, "No te has identificado correctamente")

        return render(request, 'users/login.html', {
            'title': "Identificate"
        })

def logout_user(request):
    logout(request)
    return redirect('login')