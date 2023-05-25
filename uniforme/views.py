from itertools import groupby

from django.shortcuts import redirect, render

from cadastro.models import Master

from .models import ItemSolicitacao, Solicitacao, Tamanho, Uniforme


def solicitar_uniformes(request):
    uniformes = Uniforme.objects.all().order_by('descricao')
    uniformes_agrupados = [
        {
            'descricao': descricao,
            'tamanhos': Tamanho.objects.filter(estoque__uniforme__descricao=descricao),
        }
        for descricao, _ in groupby(uniformes, lambda item: item.descricao)
    ]

    if request.method == 'POST':
        funcionario_id = request.POST.get('funcionario')
        usuario = request.user

        solicitacao = Solicitacao.objects.create(
            funcionario_id=funcionario_id, usuario=usuario
        )

        for item in uniformes_agrupados:
            uniforme_descricao = item['descricao']
            tamanhos = item['tamanhos']

            for tamanho in tamanhos:
                quantidade_key = f'quantidade_{uniforme_descricao}_{tamanho.id}'
                quantidade = int(request.POST.get(quantidade_key, 0))

                if quantidade > 0:
                    uniforme = Uniforme.objects.get(
                        descricao=uniforme_descricao)

                    ItemSolicitacao.objects.create(
                        solicitacao=solicitacao,
                        uniforme=uniforme,
                        tamanho=tamanho,
                        quantidade=quantidade
                    )

        return redirect('sucesso')  # Redireciona para uma página de sucesso

    funcionarios = Master.objects.all()

    return render(request, 'uniforme/solicitar_uniformes.html', {
        'uniformes_agrupados': uniformes_agrupados,
        'funcionarios': funcionarios
    })
