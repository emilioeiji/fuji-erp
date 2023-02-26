from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .master_form import MasterForm, PerfilForm
from .models import Master, Perfil


def cadastro_master(request):
    if request.method == 'POST':

        mt = MasterForm(request.POST)
        perfil = PerfilForm(request.POST)

        if mt.is_valid():
            usr = User.objects.create_user(
                first_name=mt.cleaned_data['nomeRomanji'],
                username=mt.cleaned_data['codigoEmpregado'],
                password=str('teste123')
            )

            master = Master(
                codigoEmpregado=mt.cleaned_data['codigoEmpregado'],
                nomeJapones=mt.cleaned_data['nomeJapones'],
                nomeRomanji=mt.cleaned_data['nomeRomanji'],
                dataInicioUnidade=mt.cleaned_data['dataInicioUnidade'],
                dataDesligamentoUnidade=mt.cleaned_data['dataDesligamentoUnidade'],
                dataDAposentadoria=mt.cleaned_data['dataDAposentadoria'],
                observacoes=mt.cleaned_data['observacoes'],
                genero=mt.cleaned_data['genero'],
                sexo=mt.cleaned_data['sexo'],
                turno=mt.cleaned_data['turno'],
                cdLocalIntegrado=mt.cleaned_data['cdLocalIntegrado'],
                codigoClassificacaoPreco=mt.cleaned_data['codigoClassificacaoPreco'],
                codigoLocalTrabalho=mt.cleaned_data['codigoLocalTrabalho'],
                paisCidadania=mt.cleaned_data['paisCidadania'],
                salarioHR=mt.cleaned_data['salarioHR'],
                novaDataChegada=mt.cleaned_data['novaDataChegada'],
                precoUnitario=mt.cleaned_data['precoUnitario'],
                reentrada=mt.cleaned_data['reentrada'],
                dataIngressaoFA=mt.cleaned_data['dataIngressaoFA'],
                dataNascimento=mt.cleaned_data['dataNascimento'],
                nomeEmpresa=mt.cleaned_data['nomeEmpresa'],
                nomeKana=mt.cleaned_data['nomeKana'],
                nomeProcesso=mt.cleaned_data['nomeProcesso'],
                codigoCdMurata=mt.cleaned_data['codigoCdMurata'],
                empregadoFinalMes=mt.cleaned_data['empregadoFinalMes'],
                andarPredioTrabalho=mt.cleaned_data['andarPredioTrabalho'],
                classificacaoContrato=mt.cleaned_data['classificacaoContrato'],
                categoriaGerente=mt.cleaned_data['categoriaGerente'],
                afiliacao=mt.cleaned_data['afiliacao'],
                codigoORDIA=mt.cleaned_data['codigoORDIA'],
                dataInicioTrabalhoExpedicao=mt.cleaned_data['dataInicioTrabalhoExpedicao'],
                codigoFuncionarioCD=mt.cleaned_data['codigoFuncionarioCD'],
                codigoEscritorio=mt.cleaned_data['codigoEscritorio'],
                salarioBrutoHR=mt.cleaned_data['salarioBrutoHR'],
                entradaCategoria=mt.cleaned_data['entradaCategoria'],
                dao=mt.cleaned_data['dao'],
                categoriaRecrutamento=mt.cleaned_data['categoriaRecrutamento'],
                quantiaPaga=mt.cleaned_data['quantiaPaga'],
                icCard=mt.cleaned_data['icCard'],
                unidadeCard=mt.cleaned_data['unidadeCard'],
                numeroAs=mt.cleaned_data['numeroAs'],
                dataConversao=mt.cleaned_data['dataConversao'],
            )

            perl = Perfil(
                foto=perfil.cleaned_data['foto'],
                user=usr
            )

            perl.save()
            master.save()
        else:
            return HttpResponse('Erro')

    else:
        return render(request, 'cadastro/cadastro_master.html', {'form': MasterForm(), 'form_perfil': PerfilForm()})
