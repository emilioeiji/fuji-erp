from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('calendario/<int:pk>/', views.CalendarioDetailView.as_view(),
         name='calendario_detail'),
    path('adicionar_mes/', views.adicionar_mes, name='adicionar_mes'),
    path('listar_funcionarios/', views.lista_funcionario_calendario,
         name='listar_funcionarios'),
    path('adicionar_funcionario/', views.adicionar_funcionario_calendario,
         name='adicionar_funcionario'),
    path('editar_funcionario/<int:funcionario_calendario_id>/',
         views.editar_funcionario_calendario, name='editar_funcionario_calendario'),
    path('excluir_funcionario/<int:funcionario_calendario_id>/',
         views.excluir_funcionario_calendario, name='excluir_funcionario_calendario'),
    path('editar_calendario/', views.editar_calendario,
         name='editar_calendario'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
