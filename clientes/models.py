from django.contrib import auth
from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

class Cliente(models.Model):
    
    AGENDADO =  (
        ("S", "Sim"),
        ("N", "Não"),
    )

    
    atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=50)
    email= models.EmailField(max_length=50, null=True, blank=True)
    agendado = models.CharField(max_length=50, choices=AGENDADO)
    data = DateTimeField(auto_now_add=True)
    observações = models.TextField()
    
    def __str__(self):
        return self.nome