from django.shortcuts import render, redirect
from .models import *
from .forms import EntrarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required(login_url='entrar/')
def index(request):
    return render(request, 'index.html')

def entrar(request):
    form = EntrarForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = EntrarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usuário')
            password = form.cleaned_data.get('senha')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login (request, user)
                return redirect('index')
            else:
                messages.error(request, "Dados inválidos!")           
    return render(request, 'auth-normal-sign-in.html', context)

@login_required(login_url='entrar/')
def sair(request):
    logout(request)
    return redirect('entrar')


def cadastrar_cliente(request):
    return render(request, 'index.html')