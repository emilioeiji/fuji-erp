from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse

from .models import Space, Tema, Topico


@login_required()
def space(request):
    spaces = Space.objects.all().order_by('area')

    context = {
        'spaces': spaces,
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
    topicos = Topico.objects.filter(tema_id=tema_id).order_by('topico')

    context = {
        'topicos': topicos,
    }

    return render(request, 'space/lista_tema.html', context)
