from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from contas.models import Perfil


class Unidade(models.Model):
    unidade = models.CharField(max_length=10, help_text="Unidade Murata")

    def __str__(self):
        return self.unidade


class Turno(models.Model):
    turno = models.CharField(max_length=10, help_text="Turno de trabalho")

    def __str__(self):
        return self.turno


class GrupoFolga(models.Model):
    grupoFolga = models.CharField(max_length=1, help_text="Grupo de folga")

    class Meta:
        ordering = ['grupoFolga']

    def __str__(self):
        return self.grupoFolga


class Linha(models.Model):
    linha = models.CharField(max_length=10, help_text="Linha ou sessao")

    class Meta:
        ordering = ['linha']

    def __str__(self):
        return self.linha


class Area(models.Model):
    linha = models.ForeignKey(Linha, on_delete=models.PROTECT)
    area = models.CharField(max_length=10, help_text="Area da linha")

    class Meta:
        ordering = ['area']

    def __str__(self):
        return self.area


class Setor(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    setor = models.CharField(max_length=10, help_text="Setor da Area")

    def __str__(self):
        return self.setor


class CdLocalIntegrado(models.Model):
    codigoCdIntegrado = models.IntegerField(unique=True)
    nome = models.CharField(max_length=20, help_text="CD Local Integrado")

    def __str__(self):
        return str(self.codigoCdIntegrado) + " " + self.nome


class ClassificacaoPreco(models.Model):
    codigoClassificacaoPreco = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.codigoClassificacaoPreco)


class PrecoUnitario(models.Model):
    nomePrecoUnitario = models.CharField(
        max_length=20, unique=True, help_text="Preco integrado funcao")
    precoUnitario = models.IntegerField()

    class Meta:
        ordering = ['nomePrecoUnitario']

    def __str__(self):
        return self.nomePrecoUnitario + " " + str(self.precoUnitario)


class NomeProcesso(models.Model):
    nomeProcesso = models.CharField(max_length=20, help_text="Nome processo")

    class Meta:
        ordering = ['nomeProcesso']

    def __str__(self):
        return self.nomeProcesso


class Escritorio(models.Model):
    codigoEscritorio = models.IntegerField(unique=True)
    nomeEscritorio = models.CharField(
        max_length=20, help_text="Nome do escritorio")

    def __str__(self):
        return str(self.codigoEscritorio) + " " + self.nomeEscritorio


class Genero(models.Model):
    nomeGenero = models.CharField(max_length=20, help_text="Nome Genero")

    def __str__(self):
        return self.nomeGenero


class Sexo(models.Model):
    nomeSexo = models.CharField(max_length=10, help_text="Sexo do Colaborador")

    def __str__(self):
        return self.nomeSexo


class LocalTrabalho(models.Model):
    codigoLocalTrabalho = models.IntegerField(primary_key=True)
    nomeLocalTrabalho = models.CharField(
        max_length=20, help_text="Nome abreviado")

    def __str__(self):
        return str(self.codigoLocalTrabalho) + " " + self.nomeLocalTrabalho


class PostoTrabalho(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    posto = models.CharField(max_length=20)
    horasNormais = models.IntegerField()
    horasExtras = models.IntegerField()
    SIM = 'S'
    NAO = 'N'
    cobranca_choices = [
        (SIM, 'Sim'),
        (NAO, 'Não'),
    ]
    cobranca = models.CharField(
        max_length=1,
        choices=cobranca_choices,
        default=SIM,
    )

    class Meta:
        ordering = ['-cobranca', 'posto']
        constraints = [
            models.UniqueConstraint(
                fields=['area', 'posto'], name='unique_posto_combination'
            )
        ]

    def __str__(self):
        return str(self.posto)


class PontoOnibus(models.Model):
    numeroOnibus = models.IntegerField()
    pontoOnibus = models.CharField(max_length=100)

    class Meta:
        ordering = ['numeroOnibus']
        constraints = [
            models.UniqueConstraint(
                fields=['numeroOnibus', 'pontoOnibus'], name='unique_ponto_onibus_combination'
            )
        ]

    def __str__(self):
        return f"{ self.numeroOnibus } - { self.pontoOnibus }"


class Master(models.Model):
    codigoEmpregado = models.IntegerField(primary_key=True)
    nomeJapones = models.CharField(max_length=30, help_text="Nome em Japones")
    nomeRomanji = models.CharField(max_length=30, help_text="Nome em Romanji")
    dataInicioUnidade = models.DateField()
    dataDesligamentoUnidade = models.DateField(blank=True, null=True)
    dataDAposentadoria = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    cdLocalIntegrado = models.ForeignKey(
        CdLocalIntegrado, on_delete=models.PROTECT)
    codigoClassificacaoPreco = models.ForeignKey(
        ClassificacaoPreco, on_delete=models.PROTECT)
    codigoLocalTrabalho = models.ForeignKey(
        LocalTrabalho, on_delete=models.PROTECT, blank=True, null=True)
    paisCidadania = models.CharField(max_length=20, help_text="Pais de origem")
    salarioHR = models.IntegerField()
    novaDataChegada = models.DateField(blank=True, null=True)
    precoUnitario = models.ForeignKey(PrecoUnitario, on_delete=models.PROTECT)
    reentrada = models.CharField(max_length=1)
    dataIngressaoFA = models.DateField(blank=True, null=True)
    dataNascimento = models.DateField(blank=True, null=True)
    nomeEmpresa = models.CharField(
        max_length=30, help_text="Nome da Empresa", blank=True, null=True)
    nomeKana = models.CharField(
        max_length=30, help_text="Nome em Kana", blank=True, null=True)
    nomeProcesso = models.ForeignKey(NomeProcesso, on_delete=models.PROTECT)
    codigoCdMurata = models.CharField(max_length=10, help_text="Codigo FJ")
    empregadoFinalMes = models.CharField(max_length=10, blank=True, null=True)
    andarPredioTrabalho = models.ForeignKey(Linha, on_delete=models.PROTECT)
    # Anos decorridos, formula com base na entrada
    # Meses decorridos, formula com base na entrada
    classificacaoContrato = models.IntegerField()
    categoriaGerente = models.IntegerField(blank=True, null=True)
    afiliacao = models.ForeignKey(Area, on_delete=models.PROTECT)
    codigoORDIA = models.IntegerField()
    dataInicioTrabalhoExpedicao = models.DateField(blank=True, null=True)
    codigoFuncionarioCD = models.IntegerField()
    codigoEscritorio = models.ForeignKey(Escritorio, on_delete=models.PROTECT)
    salarioBrutoHR = models.IntegerField(blank=True, null=True)
    # Tempo decorrido, puxar com formulario
    entradaCategoria = models.CharField(max_length=10)
    dao = models.CharField(max_length=10, blank=True, null=True)
    categoriaRecrutamento = models.CharField(max_length=20)
    quantiaPaga = models.IntegerField(blank=True, null=True)
    icCard = models.IntegerField()
    unidadeCard = models.CharField(max_length=10)
    numeroAs = models.IntegerField(blank=True, null=True)
    classificacaoContrato = models.CharField(max_length=10)
    dataConversao = models.DateField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True,
                             default='', upload_to='cadastro/fotos')

    def __str__(self):
        return str(self.codigoEmpregado) + " " + self.nomeRomanji + " " + self.nomeJapones


@receiver(post_save, sender=Master)
def criar_usuario_master(sender, instance, created, **kwargs):
    if created:
        username = instance.codigoEmpregado
        password = instance.dataNascimento.strftime('%Y%m%d')
        user = User.objects.create_user(username=username, password=password)
        perfil = Perfil.objects.create(
            usuario=user, area=instance.afiliacao, cargo=instance.nomeProcesso, foto_perfil=instance.foto)


class MasterApartamentos(models.Model):
    numero = models.IntegerField(primary_key=True)
    propriedadesCD = models.CharField(max_length=20)
    nomeApartamento = models.CharField(max_length=30)
    numeroApartamento = models.IntegerField()
    r = models.IntegerField()
    p = models.IntegerField()
    custoServicoPublico = models.IntegerField()
    dgs = models.IntegerField()
    valorTransferenciaMEnsal = models.IntegerField()
    taxaAdministracao = models.IntegerField()
    alugelEquipamento = models.IntegerField()
    valorEstacionamento = models.IntegerField()
    lga = models.IntegerField()
    valorAluguel = models.IntegerField()
    totalArrecadado = models.IntegerField()
    # Data entrada
    # Data saida
    codigoEmpregado = models.ForeignKey(Master, on_delete=models.PROTECT)
    telefone = models.IntegerField()
    cep = models.IntegerField()
    endereco = models.CharField(max_length=30)
    pontoOnibus = models.ForeignKey(PontoOnibus, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.codigoEmpregado)
