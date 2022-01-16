from django.contrib import admin
from .models import Contato, Venda, FormaPagamento

admin.site.register(Contato)
admin.site.register(Venda)
admin.site.register(FormaPagamento)
