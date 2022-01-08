from django import forms

class EntrarForm(forms.Form):
    usuário = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nome de usuário',
        }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '********',
        }))
   