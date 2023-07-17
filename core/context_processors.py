from contas.models import Perfil
from space.models import LeituraMensagem


def mensagens_nao_lidas(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.get(usuario=request.user)
        mensagens_nao_lidas = LeituraMensagem.objects.filter(
            usuario=request.user,
            lida=False,
            mensagem__topico__tema__space__area__area=perfil.area
        ).count()
    else:
        mensagens_nao_lidas = 0

    return {'mensagens_nao_lidas': mensagens_nao_lidas}
