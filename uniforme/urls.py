from django.urls import path

from . import views

urlpatterns = [
    path('solicitar/', views.solicitar_uniformes, name='solicitar_uniformes'),
    path('solicitacoes/', views.listar_solicitacoes,
         name='listar_solicitacoes'),
    path('solicitacao/<int:id_solicitacao>/', views.detalhar_solicitacao,
         name='detalhar_solicitacao'),
]
