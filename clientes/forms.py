from django import forms
from django.db import models
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
   


