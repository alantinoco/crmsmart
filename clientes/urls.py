from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),
    path('cadastro/primeiro-atendimento/', views.primeiro_atendimento, name='primeiro_atendimento'),
    #path('cadastro/agendamento/', views.cadastrar_agendamento, name='cadastrar_cliente'),
]