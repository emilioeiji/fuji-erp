from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from contas.models import Perfil

from .models import LeituraMensagem, Mensagem, Space, Tema, Topico


@login_required()
def space(request):
    spaces = Space.objects.all().order_by('area')
    perfil = Perfil.objects.get(usuario=request.user)

    context = {
        'spaces': spaces,
        'perfil': perfil,
    }

    return render(request, 'space/space.html', context)


@login_required()
def lista_mensagens(request, space_id):
    try:
        space = Space.objects.get(id=space_id)
    except Space.DoesNotExist:
        return render(request, 'space/error.html', {'error_message': 'Espaço não encontrado'})

    # Verifique se o perfil do usuário corresponde à área do espaço
    if request.user.perfil.area != space.area.area and space.area.area != 'Geral':
        return render(request, 'space/error.html', {'error_message': 'Acesso restrito'})

    temas = Tema.objects.filter(space_id=space_id).order_by('nome')
    space_id = space_id

    context = {
        'temas': temas,
        'space_id': space_id,
    }

    return render(request, 'space/lista_mensagens.html', context)


@login_required()
def conteudo_topico(request, space_id, tema_id):
    temas = Tema.objects.filter(space_id=space_id).order_by('nome')
    space_id = space_id
    topico = get_object_or_404(Topico, id=tema_id)
    mensagens = topico.mensagem_set.order_by('-data_hora_resposta')

    # Obter IDs das mensagens já lidas pelo usuário
    mensagens_lidas_ids = set(LeituraMensagem.objects.filter(
        usuario=request.user, mensagem__topico=topico).values_list('mensagem', flat=True))

    for mensagem in mensagens:
        mensagem.lida = mensagem.id in mensagens_lidas_ids

        for resposta in mensagem.respostas.all():
            resposta.lida = resposta.id in mensagens_lidas_ids

    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        nova_mensagem = Mensagem(
            topico=topico, usuario=request.user, mensagem=mensagem)
        nova_mensagem.save()
        return redirect('conteudo_topico', space_id=space_id, tema_id=tema_id)

    context = {
        'temas': temas,
        'topico': topico,
        'space_id': space_id,
        'tema_id': tema_id,
        'mensagens': mensagens,
    }

    return render(request, 'space/conteudo_topico.html', context)


@login_required()
def marcar_mensagem_lida(request, space_id, tema_id, mensagem_id):
    mensagem = get_object_or_404(Mensagem, id=mensagem_id)
    leitura_mensagem = LeituraMensagem.objects.filter(
        mensagem=mensagem, usuario=request.user
    ).first()

    if leitura_mensagem:
        leitura_mensagem.lida = True
        leitura_mensagem.save()

    return redirect('conteudo_topico',
                    space_id=space_id,
                    tema_id=tema_id)


@login_required()
def adicionar_resposta(request, space_id, tema_id, topico_id, mensagem_id):
    topico = get_object_or_404(Topico, id=topico_id)
    mensagem_original = get_object_or_404(Mensagem, id=mensagem_id)

    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        nova_resposta = Mensagem(
            topico=topico,
            usuario=request.user,
            mensagem=mensagem,
            mensagem_original=mensagem_original,
            data_hora_resposta=timezone.now()  # Define a data e hora da resposta
        )
        nova_resposta.save()

        # Atualiza o campo data_hora_resposta da mensagem original para a data da resposta
        mensagem_original.data_hora_resposta = nova_resposta.data_hora_resposta
        mensagem_original.save()

        return redirect('conteudo_topico', space_id=space_id, tema_id=tema_id)

    context = {
        'topico': topico,
        'mensagem_original': mensagem_original,
        'space_id': space_id,
        'tema_id': tema_id,
    }

    return render(request, 'space/adicionar_resposta.html', context)
