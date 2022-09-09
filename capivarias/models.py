from django.db import models
from django.utils import timezone


# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Capivaria(models.Model):
    titulo = models.CharField(max_length=20)
    descricao_curta = models.CharField(max_length=35)
    data_hora = models.DateTimeField(default=timezone.now)
    img_final = models.TextField()
    autor = models.CharField(max_length=35)
    conteudo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo