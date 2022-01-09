from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),
    path('cadastro/cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
]