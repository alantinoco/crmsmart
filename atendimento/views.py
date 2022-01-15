from django.shortcuts import render, redirect
from .forms import PrimeiroAtendimentoForm, AgendamentoForm, AtendimentoPresencialForm


def primeiro_atendimento(request):
    form = PrimeiroAtendimentoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = PrimeiroAtendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'primeiro-atendimento.html', context)


def cadastrar_agendamento(request):
    form = AgendamentoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'atendimento/cadastrar-agendamento.html', context)


def cadastrar_atendimento(request):
    form = AtendimentoPresencialForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = AtendimentoPresencialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'atendimento/cadastrar-atendimento.html', context)