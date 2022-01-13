from django import forms
from .models import Agendamento, AtendimentoPresencial


class AgendamentoForm(forms.ModelForm):
    data = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
    class Meta:
        model = Agendamento
        fields = '__all__'

class AtendimentoPresencialForm(forms.ModelForm):
    class Meta:
        model = AtendimentoPresencial
        fields = '__all__'