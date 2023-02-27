from django.db import models

from cadastro.models import Master, PostoTrabalho


class Calendario(models.Model):
    funcionario = models.ForeignKey(Master, on_delete=models.CASCADE)
    data = models.DateField()
    posto_de_trabalho = models.ForeignKey(
        PostoTrabalho, on_delete=models.CASCADE)
