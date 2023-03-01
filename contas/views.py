from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render


def perfil(request):
    return HttpResponse('Perfil')


def processa_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'username': username,
                'password': password
            }
            messages.add_message(
                request=request, message='Usuário ou senha incorretos.', level=messages.ERROR)
            return render(request, 'contas/login.html', context)

    return render(request, 'contas/login.html')


def processa_logout(request):

    storage = messages.get_messages(request)

    for message in storage:
        pass

    logout(request)
    return redirect('login')


def processa_redirect_home(request):
    return redirect('home')
