from django.shortcuts import render, redirect
from .forms import ContatoForm, VendaForm
from .models import Contato, Venda


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


def visualizar_contatos(request):

    contatos = Contato.objects.all()

    context = {
        'contatos': contatos,
    }

    return render(request, 'atendimento/visualizar/visualizar-contatos.html', context)


def visualizar_contato(request, pk):
    contato = Contato.objects.get(id=pk)
    return render(request, 'atendimento/visualizar/visualizar-contato.html', {'contato': contato})



def visualizar_vendas(request):
    return render(request, 'atendimento/visualizar/visualizar-vendas.html')


