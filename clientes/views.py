from django.shortcuts import render, redirect
from .models import *
from atendimento.models import Contato, Venda
from .forms import EntrarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from atendimento.filters import ContatoFilter
import datetime



@login_required(login_url='entrar/')
def index(request):
    hoje = datetime.datetime.now()
    agendamentos = Contato.objects.all()
    contatos = len(str(Contato.objects.filter(data_de_criação=hoje)))
    print(contatos)
    agendados = str(len(Contato.objects.filter(agendado="S", data=hoje)))
    # agendamentos = Contato.objects.filter(data=hoje)
    não_agendados = str(len(Contato.objects.filter(agendado="N", data=hoje)))

    filter = ContatoFilter(request.GET, queryset=agendamentos)


    context = {
        "agendamentos": agendamentos,
        "contatos": contatos,
        "agendados": agendados,
        "não_agendados": não_agendados,
        'filter': filter,
    }
   
    return render(request, 'index.html', context)



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

