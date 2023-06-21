from datetime import datetime

from dateutil import relativedelta
from django.db import models

from cadastro.models import GrupoFolga, Master, PostoTrabalho


class FuncionarioCalendario(models.Model):
    funcionario = models.ForeignKey(Master, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoFolga, on_delete=models.CASCADE)

    class Meta:
        ordering = [
            'grupo',
            'funcionario'
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['funcionario', 'grupo'], name='unique_calendario_funcionario'
            )
        ]

    def __str__(self):
        return f"{self.funcionario.codigoEmpregado} - {self.funcionario.nomeRomanji} - {self.grupo} - {self.funcionario.nomeProcesso}"


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

    class Meta:
        ordering = ['-mes', '-ano']

    def __str__(self):
        return f"{self.mes} - {self.ano}"


class DiaCalendario(models.Model):
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    data = models.DateField()

    class Meta:
        ordering = ['data', '-calendario']
        constraints = [
            models.UniqueConstraint(
                fields=['calendario', 'data'], name='unique_calendario_dia'
            )
        ]

    def __str__(self):
        return f"{self.data}"


class Alocacao(models.Model):
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    dia = models.ForeignKey(DiaCalendario, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(
        FuncionarioCalendario, on_delete=models.CASCADE)
    posto_trabalho = models.ForeignKey(PostoTrabalho, on_delete=models.CASCADE)
