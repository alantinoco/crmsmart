from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
    path('atendimentos/', include('atendimento.urls')),
    path('cursos/', include('escola.urls')),
]
