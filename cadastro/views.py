from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .master_form import MasterApForm, MasterForm
from .models import Master, MasterApartamentos


@login_required()
def cadastro_master(request):
    if request.method == 'POST':

        mt = MasterForm(request.POST, request.FILES)

        if mt.is_valid():

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
                foto=mt.cleaned_data['foto'],
            )

            master.save()
            return redirect('cadastro_master')
        else:
            return HttpResponse('Erro')

    else:
        return render(request, 'cadastro/cadastro_master.html', {'form': MasterForm()})


@login_required()
def listar_mt(request):
    mts = Master.objects.all().order_by('nomeRomanji')

    context = {
        'mts': mts,
    }

    return render(request, 'cadastro/listar_mt.html', context)


@login_required()
def editar_master(request, codigo_empregado):
    master = Master.objects.get(codigoEmpregado=codigo_empregado)
    form = MasterForm(instance=master)

    if request.method == 'POST':
        form = MasterForm(request.POST, instance=master)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadas com sucesso.')
            return redirect('listar_mt')

    return render(request, 'cadastro/editar_master.html', {'form': form, 'master': master})


@login_required()
def excluir_master(request, codigo_empregado):
    master = Master.objects.get(codigoEmpregado=codigo_empregado)

    if request.method == 'POST':
        master.delete()
        messages.success(request, 'Cadastro excluído com sucesso.')
        return redirect('listar_mt')

    return render(request, 'cadastro/excluir_master.html', {'master': master})


@login_required()
def listar_mt_apto(request):
    mt_aptos = MasterApartamentos.objects.all().order_by('codigoEmpregado')

    context = {
        'mt_aptos': mt_aptos,
    }

    return render(request, 'cadastro/listar_mt_apto.html', context)


@login_required()
def cadastro_master_apto(request):
    if request.method == 'POST':

        mt = MasterApForm(request.POST, request.FILES)

        if mt.is_valid():

            master = MasterApartamentos(
                codigoEmpregado=mt.cleaned_data['codigoEmpregado'],
                propriedadesCD=mt.cleaned_data['propriedadesCD'],
                nomeApartamento=mt.cleaned_data['nomeApartamento'],
                numeroApartamento=mt.cleaned_data['numeroApartamento'],
                r=mt.cleaned_data['r'],
                p=mt.cleaned_data['p'],
                custoServicoPublico=mt.cleaned_data['custoServicoPublico'],
                dgs=mt.cleaned_data['dgs'],
                valorTransferenciaMEnsal=mt.cleaned_data['valorTransferenciaMEnsal'],
                taxaAdministracao=mt.cleaned_data['taxaAdministracao'],
                alugelEquipamento=mt.cleaned_data['alugelEquipamento'],
                valorEstacionamento=mt.cleaned_data['valorEstacionamento'],
                lga=mt.cleaned_data['lga'],
                valorAluguel=mt.cleaned_data['valorAluguel'],
                totalArrecadado=mt.cleaned_data['totalArrecadado'],
                telefone=mt.cleaned_data['telefone'],
                cep=mt.cleaned_data['cep'],
                endereco=mt.cleaned_data['endereco'],
                pontoOnibus=mt.cleaned_data['pontoOnibus'],
            )

            master.save()
            return redirect('cadastro_master_apto')
        else:
            errors = mt.errors.as_data()
            error_messages = []
            for field, error_list in errors.items():
                for error in error_list:
                    error_messages.append(f"{field}: {error}")
            error_message = "<br>".join(error_messages)
            return HttpResponse(f"Erro: {error_message}")

    else:
        return render(request, 'cadastro/cadastro_master_apto.html', {'form': MasterApForm()})


@login_required()
def editar_master_apto(request, numero_apto):
    mt_apto = MasterApartamentos.objects.get(numero=numero_apto)
    form = MasterApForm(instance=mt_apto)

    if request.method == 'POST':
        form = MasterApForm(request.POST, instance=mt_apto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadas com sucesso.')
            return redirect('listar_mt_apto')

    return render(request, 'cadastro/editar_mt_apto.html', {'form': form, 'mt_apto': mt_apto})


@login_required()
def excluir_master_apto(request, numero_apto):
    mt_apto = MasterApartamentos.objects.get(numero=numero_apto)

    if request.method == 'POST':
        mt_apto.delete()
        messages.success(request, 'Cadastro excluído com sucesso.')
        return redirect('listar_mt_apto')

    return render(request, 'cadastro/excluir_mt_apto.html', {'mt_apto': mt_apto})


@login_required()
def detalhar_mt_apto(request, numero_apto):
    mt_apto = get_object_or_404(MasterApartamentos, numero=numero_apto)
    context = {'mt_apto': mt_apto}
    return render(request, 'cadastro/detalhar_mt_apto.html', context)


@login_required()
def detalhar_master(request, codigo_empregado):
    master = get_object_or_404(Master, codigoEmpregado=codigo_empregado)
    context = {'master': master}
    return render(request, 'cadastro/detalhar_master.html', context)
