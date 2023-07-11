import calendar
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView

from cadastro.models import GrupoFolga, Master

from .models import Alocacao, Calendario, DiaCalendario, FuncionarioCalendario


@login_required()
def lista_funcionario_calendario(request, mes, ano):
    funcionarios = FuncionarioCalendario.objects.filter(
        mes=mes, ano=ano).order_by('grupo', 'funcionario')
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
        'mes': mes,
        'ano': ano
    }
    return render(request, 'calendario/listar_funcionarios.html', context)


@login_required()
def adicionar_funcionario_calendario(request, mes, ano):
    if request.method == 'POST':
        funcionario_codigo = request.POST.get('funcionario')
        grupo_id = request.POST.get('grupo')

        funcionario = Master.objects.get(codigoEmpregado=funcionario_codigo)
        grupo = GrupoFolga.objects.get(id=grupo_id)

        if FuncionarioCalendario.objects.filter(funcionario_id=funcionario.codigoEmpregado, mes=mes, ano=ano).exists():
            return redirect('listar_funcionarios', mes=mes, ano=ano)

        FuncionarioCalendario.objects.create(
            funcionario=funcionario, grupo=grupo, mes=mes, ano=ano)
        return redirect('listar_funcionarios', mes=mes, ano=ano)

    funcionarios = Master.objects.all()
    grupos = GrupoFolga.objects.all()

    context = {
        'funcionarios': funcionarios,
        'grupos': grupos,
    }
    return render(request, 'calendario/adicionar_funcionario.html', context)


@login_required()
def editar_funcionario_calendario(request, funcionario_calendario_id):
    funcionario_calendario = FuncionarioCalendario.objects.get(
        id=funcionario_calendario_id)

    if request.method == 'POST':
        funcionario_codigo = request.POST.get('funcionario')
        grupo_id = request.POST.get('grupo')

        funcionario = Master.objects.get(codigoEmpregado=funcionario_codigo)
        grupo = GrupoFolga.objects.get(id=grupo_id)

        funcionario_calendario.funcionario = funcionario
        funcionario_calendario.grupo = grupo
        funcionario_calendario.save()

        return redirect('listar_funcionarios')

    funcionarios = Master.objects.all()
    grupos = GrupoFolga.objects.all()

    context = {
        'funcionario_calendario': funcionario_calendario,
        'funcionarios': funcionarios,
        'grupos': grupos,
    }
    return render(request, 'calendario/editar_funcionario.html', context)


@login_required()
def excluir_funcionario_calendario(request, funcionario_calendario_id):
    funcionario_calendario = FuncionarioCalendario.objects.get(
        id=funcionario_calendario_id)

    if request.method == 'POST':
        funcionario_calendario.delete()
        messages.success(request, 'Cadastro excluído com sucesso.')
        return redirect('listar_funcionarios')

    return render(request, 'calendario/excluir_funcionario.html', {'funcionario_calendario': funcionario_calendario})


@login_required()
def calendario(request):
    calendario = Calendario.objects.all().order_by('-ano', '-mes')

    context = {
        'calendario': calendario,
    }

    return render(request, 'calendario/calendario.html', context)


class CalendarioDetailView(DetailView):
    model = Calendario
    template_name = 'calendario/calendario_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendario = self.object
        matriz_alocacao = calendario.obter_matriz_alocacao()
        funcionarios = FuncionarioCalendario.objects.all()
        context['matriz_alocacao'] = matriz_alocacao
        context['funcionarios'] = funcionarios
        return context


@login_required()
def calendario_mes(request):
    calendario_mes = Alocacao.objects.all().order_by('dia')
    calendario_dia = DiaCalendario.objects.filter(
        data__year=2023,
        data__month=7).order_by('data')

    context = {
        'calendario_mes': calendario_mes,
        'calendario_dia': calendario_dia,
    }

    return render(request, 'calendario/calendario_mes.html', context)


@login_required()
def adicionar_mes(request):
    if request.method == 'POST':
        # Obtenha o mês e o ano do formulário
        mes = int(request.POST.get('mes'))
        ano = int(request.POST.get('ano'))

        # Crie uma instância do calendário
        calendario = Calendario.objects.criar_calendario(mes, ano)

        url = reverse('calendario_detail', args=[calendario.id])

        # Redirecione para a página de detalhes do calendário recém-criado
        return redirect(url)

    # Renderize o template para exibir o formulário de adição de mês
    return render(request, 'calendario/adicionar_mes.html')


@login_required()
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
