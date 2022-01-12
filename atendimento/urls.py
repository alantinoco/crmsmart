from django.urls import path
from . import views

urlpatterns = [
     path('cadastrar-agendamento/',views.cadastrar_agendamento , name="cadastrar-agendamento"),
]