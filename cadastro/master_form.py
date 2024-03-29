from django import forms
from django.forms.models import ModelForm

from cadastro.models import (Area, CdLocalIntegrado, ClassificacaoPreco,
                             Escritorio, Genero, Linha, LocalTrabalho, Master,
                             MasterApartamentos, NomeProcesso, PontoOnibus,
                             PrecoUnitario, Sexo, Turno)


class MasterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigoEmpregado'].required = True
        self.fields['nomeRomanji'].required = True
        self.fields['dataNascimento'].required = True

    genero = forms.ModelChoiceField(
        queryset=Genero.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    sexo = forms.ModelChoiceField(
        queryset=Sexo.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    turno = forms.ModelChoiceField(
        queryset=Turno.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    cdLocalIntegrado = forms.ModelChoiceField(
        queryset=CdLocalIntegrado.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    codigoClassificacaoPreco = forms.ModelChoiceField(
        queryset=ClassificacaoPreco.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    codigoLocalTrabalho = forms.ModelChoiceField(
        queryset=LocalTrabalho.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    precoUnitario = forms.ModelChoiceField(
        queryset=PrecoUnitario.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    nomeProcesso = forms.ModelChoiceField(
        queryset=NomeProcesso.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    andarPredioTrabalho = forms.ModelChoiceField(
        queryset=Linha.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    afiliacao = forms.ModelChoiceField(
        queryset=Area.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    codigoEscritorio = forms.ModelChoiceField(
        queryset=Escritorio.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Master
        fields = [
            'codigoEmpregado',
            'nomeJapones',
            'nomeRomanji',
            'dataInicioUnidade',
            'dataDesligamentoUnidade',
            'dataDAposentadoria',
            'observacoes',
            'genero',
            'sexo',
            'turno',
            'cdLocalIntegrado',
            'codigoClassificacaoPreco',
            'codigoLocalTrabalho',
            'paisCidadania',
            'salarioHR',
            'novaDataChegada',
            'precoUnitario',
            'reentrada',
            'dataIngressaoFA',
            'dataNascimento',
            'nomeEmpresa',
            'nomeKana',
            'nomeProcesso',
            'codigoCdMurata',
            'empregadoFinalMes',
            'andarPredioTrabalho',
            'categoriaGerente',
            'afiliacao',
            'codigoORDIA',
            'dataInicioTrabalhoExpedicao',
            'codigoFuncionarioCD',
            'codigoEscritorio',
            'salarioBrutoHR',
            'entradaCategoria',
            'dao',
            'categoriaRecrutamento',
            'quantiaPaga',
            'icCard',
            'unidadeCard',
            'numeroAs',
            'classificacaoContrato',
            'dataConversao',
            'foto',
        ]
        labels = {
            'codigoEmpregado': 'Código do Empregado',
            'nomeJapones': 'Nome em Japoêns',
            'nomeRomanji': 'Nome em Romanji',
            'dataInicioUnidade': 'Data de Inicio',
            'dataDesligamentoUnidade': 'Data de Desligamento',
            'dataDAposentadoria': 'Data da Aposentadoria',
            'observacoes': 'Obs',
            'genero': 'Gênero',
            'sexo': 'Sexo',
            'turno': 'Turno',
            'cdLocalIntegrado': 'Cod Local Integrado',
            'codigoClassificacaoPreco': 'Cod Classificação Preço',
            'codigoLocalTrabalho': 'Cod Local de Trabalho',
            'paisCidadania': 'País da Cidadania',
            'salarioHR': 'Salário por Hora',
            'novaDataChegada': 'Data Chegada',
            'precoUnitario': 'Preço Unitário',
            'reentrada': 'Reentrada',
            'dataIngressaoFA': 'Data Integração',
            'dataNascimento': 'Data de Nascimento',
            'nomeEmpresa': 'Nome da Empresa',
            'nomeKana': 'Nome Kana',
            'nomeProcesso': 'Nome do Processo',
            'codigoCdMurata': 'Código Murata',
            'empregadoFinalMes': 'Empregado Final de Mês',
            'andarPredioTrabalho': 'Andaro do Prédio',
            'categoriaGerente': 'Categoria do Gerente',
            'afiliacao': 'Afiliação',
            'codigoORDIA': 'Código ORDIA',
            'dataInicioTrabalhoExpedicao': 'Data Inicio Trabalho',
            'codigoFuncionarioCD': 'Cod CD',
            'codigoEscritorio': 'Cod Escritório',
            'salarioBrutoHR': 'Salário Bruto HR',
            'entradaCategoria': 'Entrada Categoria',
            'dao': 'DAO',
            'categoriaRecrutamento': 'Categoria Recrutamento',
            'quantiaPaga': 'Quantidade Paga',
            'icCard': 'IC Card',
            'unidadeCard': 'Unidade Card',
            'numeroAs': 'Número AS',
            'classificacaoContrato': 'Classificação Contrato',
            'dataConversao': 'Data Conversão',
            'foto': 'Foto Colaborador',
        }
        widgets = {
            'codigoEmpregado': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeJapones': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeRomanji': forms.TextInput(attrs={'class': 'form-control'}),
            'dataInicioUnidade': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'dataDesligamentoUnidade': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'dataDAposentadoria': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'observacoes': forms.TextInput(attrs={'class': 'form-control'}),
            'cdLocalIntegrado': forms.TextInput(attrs={'class': 'form-control'}),
            'codigoClassificacaoPreco': forms.TextInput(attrs={'class': 'form-control'}),
            'codigoLocalTrabalho': forms.TextInput(attrs={'class': 'form-control'}),
            'paisCidadania': forms.TextInput(attrs={'class': 'form-control'}),
            'salarioHR': forms.TextInput(attrs={'class': 'form-control'}),
            'novaDataChegada': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'precoUnitario': forms.TextInput(attrs={'class': 'form-control'}),
            'reentrada': forms.TextInput(attrs={'class': 'form-control'}),
            'dataIngressaoFA': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'dataNascimento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'nomeEmpresa': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeKana': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeProcesso': forms.TextInput(attrs={'class': 'form-control'}),
            'codigoCdMurata': forms.TextInput(attrs={'class': 'form-control'}),
            'empregadoFinalMes': forms.TextInput(attrs={'class': 'form-control'}),
            'andarPredioTrabalho': forms.TextInput(attrs={'class': 'form-control'}),
            'categoriaGerente': forms.TextInput(attrs={'class': 'form-control'}),
            'afiliacao': forms.TextInput(attrs={'class': 'form-control'}),
            'codigoORDIA': forms.TextInput(attrs={'class': 'form-control'}),
            'dataInicioTrabalhoExpedicao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'codigoFuncionarioCD': forms.TextInput(attrs={'class': 'form-control'}),
            'codigoEscritorio': forms.TextInput(attrs={'class': 'form-control'}),
            'salarioBrutoHR': forms.TextInput(attrs={'class': 'form-control'}),
            'entradaCategoria': forms.TextInput(attrs={'class': 'form-control'}),
            'dao': forms.TextInput(attrs={'class': 'form-control'}),
            'categoriaRecrutamento': forms.TextInput(attrs={'class': 'form-control'}),
            'quantiaPaga': forms.TextInput(attrs={'class': 'form-control'}),
            'icCard': forms.TextInput(attrs={'class': 'form-control'}),
            'unidadeCard': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroAs': forms.TextInput(attrs={'class': 'form-control'}),
            'classificacaoContrato': forms.TextInput(attrs={'class': 'form-control'}),
            'dataConversao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }


class MasterApForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigoEmpregado'].required = True
        self.fields['nomeApartamento'].required = True
        self.fields['numeroApartamento'].required = True

    codigoEmpregado = forms.ModelChoiceField(
        queryset=Master.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    pontoOnibus = forms.ModelChoiceField(
        queryset=PontoOnibus.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = MasterApartamentos
        fields = [
            'codigoEmpregado',
            'propriedadesCD',
            'nomeApartamento',
            'numeroApartamento',
            'r',
            'p',
            'custoServicoPublico',
            'dgs',
            'valorTransferenciaMEnsal',
            'taxaAdministracao',
            'alugelEquipamento',
            'valorEstacionamento',
            'lga',
            'valorAluguel',
            'totalArrecadado',
            'telefone',
            'cep',
            'endereco',
            'pontoOnibus',
        ]

        labels = {
            'codigoEmpregado': 'Funcionário',
            'propriedadesCD': 'Código CD',
            'nomeApartamento': 'Nome do Apartamento',
            'numeroApartamento': 'Número do Apartamento',
            'r': 'R',
            'p': 'P',
            'custoServicoPublico': 'Valor Serv. Público',
            'dgs': 'DGS',
            'valorTransferenciaMEnsal': 'Valor Transf Mensal',
            'taxaAdministracao': 'Taxa de Administração',
            'alugelEquipamento': 'Aluguél Equipamento',
            'valorEstacionamento': 'Valor Estacionamento',
            'lga': 'LGA',
            'valorAluguel': 'Valor Aluguél',
            'totalArrecadado': 'Total Arrecadado',
            'telefone': 'Telefone',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'pontoOnibus': 'Ponto de Ônibus',
        }

        widgets = {
            'codigoEmpregado': forms.TextInput(attrs={'class': 'form-control'}),
            'propriedadesCD': forms.TextInput(attrs={'class': 'form-control'}),
            'nomeApartamento': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroApartamento': forms.TextInput(attrs={'class': 'form-control'}),
            'r': forms.TextInput(attrs={'class': 'form-control'}),
            'p': forms.TextInput(attrs={'class': 'form-control'}),
            'custoServicoPublico': forms.TextInput(attrs={'class': 'form-control'}),
            'dgs': forms.TextInput(attrs={'class': 'form-control'}),
            'valorTransferenciaMEnsal': forms.TextInput(attrs={'class': 'form-control'}),
            'taxaAdministracao': forms.TextInput(attrs={'class': 'form-control'}),
            'alugelEquipamento': forms.TextInput(attrs={'class': 'form-control'}),
            'valorEstacionamento': forms.TextInput(attrs={'class': 'form-control'}),
            'lga': forms.TextInput(attrs={'class': 'form-control'}),
            'valorAluguel': forms.TextInput(attrs={'class': 'form-control'}),
            'totalArrecadado': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'pontoOnibus': forms.TextInput(attrs={'class': 'form-control'}),
        }
