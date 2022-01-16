from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
    path('atendimento/', include('atendimento.urls')),
    path('curso/', include('escola.urls')),
]
