from django import forms
from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    data = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
    class Meta:
        model = Agendamento
        fields = '__all__'