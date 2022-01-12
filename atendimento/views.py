from django.shortcuts import render, redirect
from .forms import AgendamentoForm


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
    return render(request, 'form-agendamento.html', context)