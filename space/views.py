from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse

from .models import Space


@login_required()
def space(request):
    spaces = Space.objects.all().order_by('area')

    context = {
        'spaces': spaces,
    }

    return render(request, 'space/space.html', context)
