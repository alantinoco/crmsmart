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
    observações = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Agendamento(models.Model):

    HORARIOS =  (
        ("1º", "08:00 as 09:00"),
        ("2º", "09:00 as 10:00"),
        ("3º", "11:00 as 12:00"),
        ("4º", "12:00 as 13:00"),
        ("5º", "13:00 as 14:00"),
        ("6º", "14:00 as 15:00"),
        ("7º", "15:00 as 16:00"),
        ("8º", "16:00 as 17:00"),
        ("9º", "17:00 as 16:00"),
        ("10º","17:00 as 18:00"),
        ("11º","18:00 as 19:00"),
        ("12º", "ESPECIAL")
    )

    atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    data = models.DateField(auto_now_add=False, auto_now=False)
    hora = models.CharField(max_length=50, choices=HORARIOS)
    observações = models.TextField(null=True, blank=True)