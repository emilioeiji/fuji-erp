from datetime import date, datetime, timedelta

from dateutil import relativedelta
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from cadastro.models import Area, GrupoFolga, Master, PostoTrabalho


class FuncionarioCalendario(models.Model):
    funcionario = models.ForeignKey(Master, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoFolga, on_delete=models.CASCADE)
    mes = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()

    class Meta:
        ordering = [
            '-ano',
            '-mes',
            'grupo',
            'funcionario'
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['ano', 'mes', 'funcionario', 'grupo'],
                name='unique_calendario_funcionario'
            )
        ]

    def __str__(self):
        return ' - '.join([
            str(self.ano),
            str(self.mes),
            str(self.funcionario.codigoEmpregado),
            self.funcionario.nomeRomanji,
            str(self.grupo),
            str(self.funcionario.nomeProcesso)
        ])
        # return f"{self.funcionario.codigoEmpregado} - {self.funcionario.nomeRomanji} - {self.grupo} - {self.funcionario.nomeProcesso} - {self.mes}-{self.ano}"


class CalendarioManager(models.Manager):
    def criar_calendario(self, mes, ano):
        primeiro_dia = date(ano, mes, 1)
        ultimo_dia = primeiro_dia.replace(
            day=1, month=mes+1) - timedelta(days=1)

        calendario = Calendario(mes=mes, ano=ano)
        calendario.save()

        # Cria os objetos DiaCalendario para cada dia do mês
        dia_atual = primeiro_dia
        while dia_atual <= ultimo_dia:
            DiaCalendario.objects.create(
                calendario=calendario,
                data=dia_atual
            )
            dia_atual += timedelta(days=1)

        return calendario


class Calendario(models.Model):
    objects = CalendarioManager()
    mes = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    bloqueado = models.BooleanField(default=False)

    def obter_matriz_alocacao(self):
        funcionarios = FuncionarioCalendario.objects.all()
        dias = DiaCalendario.objects.filter(calendario=self)

        # Cria uma lista com os dias do mês
        primeira_linha = [str(dia.data.day) for dia in dias]

        # Inicializa a matriz com a primeira linha
        matriz_alocacao = [primeira_linha]

        for funcionario in funcionarios:
            alocacoes_funcionario = Alocacao.objects.filter(
                calendario_id=self.id, funcionario=funcionario)
            # Adiciona o nome do funcionário na primeira coluna
            linha_alocacao = [funcionario.funcionario.nomeRomanji]

            for dia in dias:
                alocacao = alocacoes_funcionario.filter(dia=dia).first()
                posto_trabalho = alocacao.posto_trabalho if alocacao else None
                linha_alocacao.append(posto_trabalho)

            matriz_alocacao.append(linha_alocacao)

        return matriz_alocacao

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
    calendario = models.ForeignKey(
        Calendario, on_delete=models.CASCADE)
    dia = models.ForeignKey(DiaCalendario, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(
        FuncionarioCalendario, on_delete=models.CASCADE)
    posto_trabalho = models.ForeignKey(PostoTrabalho, on_delete=models.CASCADE)
