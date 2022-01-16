from django.shortcuts import render, redirect
from .forms import ContatoForm, VendaForm


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
    return render(request, 'atendimento/cadastrar/contato.html', context)


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
    return render(request, 'atendimento/cadastrar/venda.html', context)