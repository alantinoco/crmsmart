from django.urls import path
from . import views

urlpatterns = [
     path('cadastrar/contato/',views.cadastrar_contato, name="cadastrar_contato"),
     path('atualizar/contato/<int:pk>/', views.atualizar_contato, name='atualizar_contato'),
     path('deletar/contato/<int:pk>/', views.deletar_contato, name='deletar_contato'),
     path('cadastrar/venda/',views.cadastrar_venda, name="cadastrar_venda"),
     path('visualizar/contatos/',views.visualizar_contatos, name="visualizar_contatos"),
     path('visualizar/contato/<int:pk>/',views.visualizar_contato, name="visualizar_contato"),
     path('visualizar/vendas/',views.visualizar_vendas, name="visualizar_vendas"),
     path('visualizar/venda/<int:pk>/',views.visualizar_venda, name="visualizar_venda"),
     path('atualizar/venda/<int:pk>/', views.atualizar_venda, name='atualizar_venda'),
     path('deletar/venda/<int:pk>/', views.deletar_venda, name='deletar_venda'),

]
