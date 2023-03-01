from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('login/', views.processa_login, name='login'),
    path('logout/', views.processa_logout, name='logout'),
    path('redirect_home/', views.processa_redirect_home, name='go_home')
]
