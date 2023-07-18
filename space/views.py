from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contas.models import Perfil

from .models import Mensagem, Space, Tema, Topico


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
def lista_space(request, space_id):
    temas = Tema.objects.filter(space_id=space_id).order_by('nome')

    context = {
        'temas': temas,
    }

    return render(request, 'space/lista_space.html', context)


@login_required()
def lista_tema(request, tema_id):
    topico = get_object_or_404(Topico, id=tema_id)
    space_id = topico.tema.space_id
    mensagens = topico.mensagem_set.order_by('-data_hora_criacao')

    for mensagem in mensagens:
        mensagem.lida = mensagem.leituramensagem_set.filter(
            usuario=request.user, lida=True).exists()

    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        nova_mensagem = Mensagem(
            topico=topico, usuario=request.user, mensagem=mensagem)
        nova_mensagem.save()
        return redirect('lista_mensagens', space_id=space_id)

    context = {
        'topico': topico,
        'mensagens': mensagens,
    }

    return render(request, 'space/lista_tema.html', context)


@login_required()
def lista_mensagens(request, space_id):
    temas = Tema.objects.filter(space_id=space_id).order_by('nome')

    context = {
        'temas': temas,
    }

    return render(request, 'space/lista_mensagens.html', context)
