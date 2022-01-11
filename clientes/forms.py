from django import forms
from django.db import models
from .models import Cliente, Agendamento
from django.contrib.auth.models import User
from django.conf import settings

class EntrarForm(forms.Form):
    usuário = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nome de usuário',
        }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '********',
        }))
   
class ClienteForm(forms.ModelForm):
    #atendente = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Cliente
        fields = [
            'atendente',
            'nome',
            'sobrenome',
            'cpf',
            'telefone',
            'email',
            'agendado',
            'observações'
        ]

class AgendamentoForm(forms.ModelForm):
    data = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
    class Meta:
        model = Agendamento
        fields = '__all__'

