from django.urls import path
from . import views

urlpatterns = [
     path('cadastrar/contato/',views.cadastrar_contato, name="cadastrar_contato"),
     path('cadastrar/venda/',views.cadastrar_venda, name="cadastrar_venda"),
     path('visualizar/contato/',views.visualizar_contato, name="visualizar_contato"),
     path('visualizar/venda/',views.visualizar_venda, name="visualizar_venda"),
]
