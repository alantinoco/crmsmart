from django.urls import path
from . import views

urlpatterns = [
     path('atendimento/cadastrar/contato/',views.cadastrar_contato , name="cadastrar_contato"),
     path('atendimento/cadastrar/venda/',views.cadastrar_venda , name="cadastrar_venda"),
]