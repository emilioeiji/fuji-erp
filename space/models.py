from django.db import models

from cadastro.models import Area, Master


class Space(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Space")

    class Meta:
        ordering = ['area']

    def __str__(self):
        return f"{self.area} - {self.nome}"
