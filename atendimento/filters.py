import django_filters
from .models import Contato

class ContatoFilter(django_filters.FilterSet):
    data_de_criação = django_filters.DateRangeFilter(lookup_expr='iexact')
    class Meta:
        model = Contato
        fields = ('data_de_criação',)