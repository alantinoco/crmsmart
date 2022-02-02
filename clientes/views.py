from django.shortcuts import render, redirect
from .models import *
from atendimento.models import Contato, Venda
from .forms import EntrarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from atendimento.filters import ContatoFilter
from datetime import date

@login_required(login_url='entrar/')
def index(request):
    hoje = date.today()
    agendamentos = Contato.objects.all()
    agendamentos_de_hoje = Contato.objects.filter(agendado='S').filter(data__contains=hoje)
    agendados = agendamentos_de_hoje.count()
    não_agendados_de_hoje = Contato.objects.filter(agendado="N").filter(data_de_criação__contains=hoje)
    não_agendados = não_agendados_de_hoje.count()
    vendas_de_hoje = Venda.objects.filter(comprou='S').filter(data__contains=hoje)
    vendas = vendas_de_hoje.count()
    contatos_de_hoje = Contato.objects.filter(data_de_criação__contains=hoje)
    contatos = contatos_de_hoje.count()
    facebook_de_hoje = Contato.objects.filter(origem="Facebook").filter(data_de_criação__contains=hoje)
    facebook = facebook_de_hoje.count()
    instagram_de_hoje = Contato.objects.filter(origem="Instagram").filter(data_de_criação__contains=hoje)
    instagram = instagram_de_hoje.count()
    faixas_de_hoje = Contato.objects.filter(origem="Faixas").filter(data_de_criação__contains=hoje)
    faixas = faixas_de_hoje.count()
    panfletos_de_hoje = Contato.objects.filter(origem="Panfletos").filter(data_de_criação__contains=hoje)
    panfletos = panfletos_de_hoje.count()
    matriz_de_hoje = Contato.objects.filter(origem="Matriz").filter(data_de_criação__contains=hoje)
    matriz = matriz_de_hoje.count()
    outros_de_hoje = Contato.objects.filter(origem="Outros").filter(data_de_criação__contains=hoje)
    outros = outros_de_hoje.count()

    filter = ContatoFilter(request.GET, queryset=agendamentos)

    context = {
        "agendamentos": agendamentos,
        "contatos": contatos,
        "agendados": agendados,
        "não_agendados": não_agendados,
        "vendas": vendas,
        "filter": filter,
        "contatos_de_hoje": contatos_de_hoje,
        "facebook": facebook,
        "instagram": instagram,
        "faixas": faixas,
        "panfletos": panfletos,
        "matriz": matriz,
        "outros": outros,
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

