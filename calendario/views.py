import calendar
from datetime import timedelta

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils import timezone

from cadastro.models import GrupoFolga, Master

from .models import Calendario, DiaCalendario, FuncionarioCalendario


def lista_funcionario_calendario(request):
    funcionarios = FuncionarioCalendario.objects.all().order_by('grupo', 'funcionario')
    for funcionario in funcionarios:
        if str(funcionario.grupo) == 'A':
            funcionario.estilo_grupo = 'bg-a'
        elif str(funcionario.grupo) == 'B':
            funcionario.estilo_grupo = 'bg-b'
        elif str(funcionario.grupo) == 'C':
            funcionario.estilo_grupo = 'bg-c'
        else:
            funcionario.estilo_grupo = ''

        if str(funcionario.funcionario.nomeProcesso) == 'ﾘﾘｰﾌ':
            funcionario.estilo_ririfu = 'bg-ririfu'
        else:
            funcionario.estilo_ririfu = ''

        if str(funcionario.funcionario.precoUnitario.nomePrecoUnitario) == 'ﾄﾚｰﾅｰ':
            funcionario.estilo_treinador = 'bg-treinador'
        else:
            funcionario.estilo_treinador = ''

        if str(funcionario.funcionario.turno) == 'Yakin':
            funcionario.estilo_turno = 'bg-noite'
        elif str(funcionario.funcionario.turno) == 'Hirukin':
            funcionario.estilo_turno = 'bg-dia'
        else:
            funcionario.estilo_turno = ''

    context = {
        'funcionarios': funcionarios,
    }
    return render(request, 'calendario/listar_funcionarios.html', context)


def adicionar_funcionario_calendario(request):
    if request.method == 'POST':
        funcionario_codigo = request.POST.get('funcionario')
        grupo_id = request.POST.get('grupo')

        funcionario = Master.objects.get(codigoEmpregado=funcionario_codigo)
        grupo = GrupoFolga.objects.get(id=grupo_id)

        if FuncionarioCalendario.objects.filter(funcionario=funcionario).exists():
            return redirect('listar_funcionarios')

        FuncionarioCalendario.objects.create(
            funcionario=funcionario, grupo=grupo)
        return redirect('listar_funcionarios')

    funcionarios = Master.objects.all()
    grupos = GrupoFolga.objects.all()

    context = {
        'funcionarios': funcionarios,
        'grupos': grupos,
    }
    return render(request, 'calendario/adicionar_funcionario.html', context)


def calendario(request):
    hoje = timezone.now().date()
    inicio_do_mes = hoje.replace(day=1)
    fim_do_mes = inicio_do_mes + timedelta(days=32)

    ano = inicio_do_mes.year
    mes = inicio_do_mes.month
    _, ultimo_dia = calendar.monthrange(ano, mes)

    dias_do_mes = [str(dia) for dia in range(1, ultimo_dia + 1)]

    calendario = DiaCalendario.objects.filter(
        calendario__ano=ano,
        calendario__mes=mes
    ).order_by('data', 'funcionario__nomeRomanji')

    return render(request, 'calendario/calendario.html', {'calendario': calendario, 'dias_do_mes': dias_do_mes})


def editar_calendario(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        funcionario_id = request.POST.get('funcionario_id')
        posto_de_trabalho = request.POST.get('posto_de_trabalho')
        calendario = DiaCalendario.objects.get(
            calendario__data=data, calendario__funcionario_id=funcionario_id)
        calendario.posto_de_trabalho = posto_de_trabalho
        calendario.save()
        return HttpResponse('Alterações salvas com sucesso.')
    else:
        return HttpResponseNotAllowed(['POST'])
