from datetime import datetime

from dateutil import relativedelta
from django.db import models

from cadastro.models import Master, PostoTrabalho


class CalendarioManager(models.Manager):
    def criar_calendario(self, mes, ano):
        primeiro_dia = datetime(ano, mes, 1).date()
        ultimo_dia = primeiro_dia + relativedelta.relativedelta(day=31)

        calendario = self.create(mes=mes, ano=ano)

        for data in daterange(primeiro_dia, ultimo_dia):
            DiaCalendario.objects.create(
                calendario=calendario,
                data=data,
                funcionario=calendario.funcionario,
                # Função para calcular o posto de trabalho
                posto_de_trabalho=calcular_posto_de_trabalho(data)
            )

        return calendario


class Calendario(models.Model):
    objects = CalendarioManager()
    mes = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    bloqueado = models.BooleanField(default=False)


class DiaCalendario(models.Model):
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    data = models.DateField()
    posto_de_trabalho = models.ForeignKey(
        PostoTrabalho, on_delete=models.CASCADE)
    dia_util = models.BooleanField(default=True)
    funcionario = models.ForeignKey(Master, on_delete=models.CASCADE)
