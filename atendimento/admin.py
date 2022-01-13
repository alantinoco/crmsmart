from django.contrib import admin
from .models import Agendamento, AtendimentoPresencial

admin.site.register(Agendamento)
admin.site.register(AtendimentoPresencial)