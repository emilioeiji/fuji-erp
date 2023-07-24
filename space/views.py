from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

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
    mensagens = topico.mensagem_set.order_by('-data_hora_criacao')

    for mensagem in mensagens:
        mensagem.lida = mensagem.leituramensagem_set.filter(
            usuario=request.user, lida=True).exists()

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
