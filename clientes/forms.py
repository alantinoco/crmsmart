from django import forms
from .models import Cliente
from django.contrib.auth.models import User

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
            'telefone',
            'email',
            'agendado',
            'observações'
        ]

