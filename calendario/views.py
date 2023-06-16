import calendar
from datetime import timedelta

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.utils import timezone

from .models import Calendario, DiaCalendario


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
