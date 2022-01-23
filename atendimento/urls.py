from django.urls import path
from . import views

urlpatterns = [
     path('cadastrar/contato/',views.cadastrar_contato, name="cadastrar_contato"),
     path('cadastrar/venda/',views.cadastrar_venda, name="cadastrar_venda"),
     path('visualizar/contatos/',views.visualizar_contatos, name="visualizar_contatos"),
     path('visualizar/contato/<int:pk>/',views.visualizar_contato, name="visualizar_contato"),
     path('visualizar/vendas/',views.visualizar_vendas, name="visualizar_vendas"),
     path('visualizar/venda/<int:pk>/',views.visualizar_venda, name="visualizar_venda"),
]
