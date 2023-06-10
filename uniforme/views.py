from django.shortcuts import get_object_or_404, redirect, render

from cadastro.models import Master

from .models import (ItemSolicitacao, Solicitacao, StatusSolicitacao, Tamanho,
                     Uniforme)


def solicitar_uniformes(request):
    uniformes = Uniforme.objects.all()
    status_solicitacao = StatusSolicitacao.objects.all()
    funcionarios = Master.objects.all()

    if request.method == 'POST':
        funcionario_id = request.POST.get('funcionario')
        status_id = request.POST.get('status')

        if funcionario_id and status_id:
            print('aqui')
            funcionario = Master.objects.get(pk=funcionario_id)
            status = StatusSolicitacao.objects.get(pk=status_id)

            solicitacao = Solicitacao.objects.create(
                usuario=request.user,
                funcionario=funcionario,
                status=status
            )

            for i in range(1, 6):
                uniforme_id = request.POST.get(f'uniforme{i}')
                quantidade = request.POST.get(f'quantidade{i}')

                if uniforme_id and quantidade:
                    uniforme = Uniforme.objects.get(pk=uniforme_id)

                    item = ItemSolicitacao.objects.create(
                        solicitacao=solicitacao,
                        uniforme_tamanho=uniforme,
                        quantidade=quantidade
                    )

            return redirect('listar_solicitacoes')

    context = {
        'uniformes': uniformes,
        'status_solicitacao': status_solicitacao,
        'funcionarios': funcionarios,
    }

    return render(request, 'uniforme/solicitar_uniformes.html', context)


def listar_solicitacoes(request):
    solicitacoes = Solicitacao.objects.all().order_by('-id_solicitacao')
    context = {'solicitacoes': solicitacoes}
    return render(request, 'uniforme/listar_solicitacoes.html', context)


def detalhar_solicitacao(request, id_solicitacao):
    solicitacao = get_object_or_404(Solicitacao, id_solicitacao=id_solicitacao)
    context = {'solicitacao': solicitacao}
    return render(request, 'uniforme/detalhar_solicitacao.html', context)


def imprimir_solicitacao(request, id_solicitacao):
    solicitacao = get_object_or_404(Solicitacao, id_solicitacao=id_solicitacao)
    context = {'solicitacao': solicitacao}
    return render(request, 'uniforme/imp_solicitacao.html', context)
