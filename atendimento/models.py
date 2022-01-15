from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from escola.models import Cursos




class FormaPagamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

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


class Agendamento(models.Model):

    HORARIOS =  (
        ("08:00 as 09:00", "08:00 as 09:00"),
        ("09:00 as 10:00", "09:00 as 10:00"),
        ("11:00 as 12:00", "11:00 as 12:00"),
        ("12:00 as 13:00", "12:00 as 13:00"),
        ("13:00 as 14:00", "13:00 as 14:00"),
        ("14:00 as 15:00", "14:00 as 15:00"),
        ("15:00 as 16:00", "15:00 as 16:00"),
        ("16:00 as 17:00", "16:00 as 17:00"),
        ("17:00 as 16:00", "17:00 as 16:00"),
        ("17:00 as 18:00","17:00 as 18:00"),
        ("18:00 as 19:00","18:00 as 19:00"),
        ("ESPECIAL", "ESPECIAL"),
    )

    atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    cliente = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=False, auto_now=False)
    horário = models.CharField(max_length=50, choices=HORARIOS)
    observações = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cliente


class AtendimentoPresencial(models.Model):

    COMPROU =  (
        ("S", "Sim"),
        ("N", "Não"),
    )

    atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(PrimeiroAtendimento, null=True, blank=True, on_delete=models.SET_NULL)
    data = models.DateTimeField(auto_now_add=True)
    curso_desejado = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
    comprou = models.CharField(max_length=50, choices=COMPROU)
    forma_de_pagamento = models.ForeignKey(FormaPagamento, null=True, blank=True, on_delete=models.SET_NULL)
    observações = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.cliente) 