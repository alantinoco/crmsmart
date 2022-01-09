from django import forms
from .models import Cliente

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
    class Meta:
        model = Cliente
        fields = '__all__'
