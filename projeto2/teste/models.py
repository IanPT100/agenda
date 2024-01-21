from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.PositiveIntegerField()
    investimento = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
