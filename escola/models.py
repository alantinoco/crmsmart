from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    descrição = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome