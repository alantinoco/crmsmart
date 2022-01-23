from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContatoForm, VendaForm
from .models import Contato, Venda

@login_required(login_url='entrar/')
def cadastrar_contato(request):
    form = ContatoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'atendimento/cadastrar/cadastrar-contato.html', context)


@login_required(login_url='entrar/')
def cadastrar_venda(request):
    form = VendaForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'atendimento/cadastrar/cadastrar-venda.html', context)


@login_required(login_url='entrar/')
def visualizar_contatos(request):

    contatos = Contato.objects.all()

    context = {
        'contatos': contatos,
    }

    return render(request, 'atendimento/visualizar/visualizar-contatos.html', context)


@login_required(login_url='entrar/')
def visualizar_contato(request, pk):
    contato = Contato.objects.get(id=pk)
    return render(request, 'atendimento/visualizar/visualizar-contato.html', {'contato': contato})


@login_required(login_url='entrar/')
def visualizar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'atendimento/visualizar/visualizar-vendas.html', {'vendas': vendas})

@login_required(login_url='entrar/')
def visualizar_venda(request, pk):
    vendas = Venda.objects.filter(id=pk)
    return render(request, 'atendimento/visualizar/visualizar-venda.html', {'vendas': vendas})



