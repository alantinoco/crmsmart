from django.urls import path
from . import views

urlpatterns = [
     path('cadastro/primeiro-atendimento/', views.primeiro_atendimento, name='primeiro_atendimento'),
     path('cadastrar-agendamento/',views.cadastrar_agendamento , name="cadastrar-agendamento"),
     path('cadastrar-atendimento/',views.cadastrar_atendimento , name="cadastrar_atendimento"),
]