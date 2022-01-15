from django.contrib import admin
from .models import PrimeiroAtendimento, Agendamento, AtendimentoPresencial, FormaPagamento

admin.site.register(Agendamento)
admin.site.register(AtendimentoPresencial)
admin.site.register(PrimeiroAtendimento)
admin.site.register(FormaPagamento)