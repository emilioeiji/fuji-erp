from django.db.models import Count, Q

from contas.models import Perfil
from space.models import LeituraMensagem


def mensagens_nao_lidas(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.get(usuario=request.user)

        consulta = Q(
            Q(usuario=request.user, lida=False, mensagem__topico__tema__space__area__area=perfil.area) |
            Q(usuario=request.user, lida=False,
              mensagem__topico__tema__space__area__area="Geral")
        )

        consulta_perfil = Q(
            usuario=request.user,
            lida=False,
            mensagem__topico__tema__space__area__area=perfil.area
        )

        consulta_geral = Q(
            usuario=request.user,
            lida=False,
            mensagem__topico__tema__space__area__area="Geral"
        )

        mensagens_nao_lidas = LeituraMensagem.objects.filter(consulta).values(
            'mensagem__topico').annotate(qtd_mensagens_nao_lidas=Count('id'))

        mensagens_perfil = LeituraMensagem.objects.filter(consulta_perfil).values(
            'mensagem__topico').annotate(qtd_mensagens_nao_lidas=Count('id'))

        mensagens_gerais = LeituraMensagem.objects.filter(consulta_geral).values(
            'mensagem__topico').annotate(qtd_mensagens_nao_lidas=Count('id'))

        total_mensagens_perfil = sum(
            mensagem['qtd_mensagens_nao_lidas'] for mensagem in mensagens_perfil)
        total_mensagens_gerais = sum(
            mensagem['qtd_mensagens_nao_lidas'] for mensagem in mensagens_gerais)
        total_mensagens_nao_lidas = total_mensagens_perfil + total_mensagens_gerais
    else:
        mensagens_nao_lidas = []
        mensagens_perfil = []
        mensagens_gerais = []
        total_mensagens_perfil = 0
        total_mensagens_gerais = 0
        total_mensagens_nao_lidas = 0

    return {
        'mensagens_nao_lidas': mensagens_nao_lidas,
        'total_mensagens_nao_lidas': total_mensagens_nao_lidas,
        'mensagens_perfil': mensagens_perfil,
        'total_mensagens_perfil': total_mensagens_perfil,
        'mensagens_gerais': mensagens_gerais,
        'total_mensagens_gerais': total_mensagens_gerais
    }
