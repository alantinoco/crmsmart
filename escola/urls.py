from django.urls import path
from . import views

urlpatterns = [
    path('todos-cursos/', views.cursos, name="todos-os-cursos")
]

