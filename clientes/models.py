from django.contrib import auth
from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from escola.models import *


class PrimeiroAtendimento(models.Model):
    
    AGENDADO =  (
        ("S", "Sim"),
        ("N", "Não"),
    )

    ORIGEM =  (
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("Panfletos", "Panfletos"),
        ("Faixas", "Faixas"),
        ("Matriz", "Matriz"),
        ("Outros", "Outros"),
    )

    atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    curso_desejado = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
    origem = models.CharField(max_length=50, choices=ORIGEM)
    agendado = models.CharField(max_length=50, choices=AGENDADO)
    data = DateTimeField(auto_now_add=True)
    observações = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
