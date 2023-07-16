from space.models import LeituraMensagem


def mensagens_nao_lidas(request):
    if request.user.is_authenticated:
        mensagens_nao_lidas = LeituraMensagem.objects.filter(
            usuario=request.user, lida=False).count()
    else:
        mensagens_nao_lidas = 0
    return {'mensagens_nao_lidas': mensagens_nao_lidas}
