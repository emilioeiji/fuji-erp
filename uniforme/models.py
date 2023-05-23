from django.db import models


class Tamanho (models.Model):
    tamanho = models.CharField(max_length=10, help_text="Descricao Uniforme")

    def __str__(self):
        return self.tamanho


class Uniforme (models.Model):
    descricao = models.CharField(max_length=50, help_text="Descricao Uniforme")
    valor = models.IntegerField()

    def __str__(self):
        return self.descricao + " - " + str(self.valor)
