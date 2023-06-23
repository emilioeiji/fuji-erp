from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('master/', views.cadastro_master, name='cadastro_master'),
    path('listar_mt', views.listar_mt, name='listar_mt'),
    path('editar-master/<int:codigo_empregado>/',
         views.editar_master, name='editar_master'),
    path('excluir-master/<int:codigo_empregado>/',
         views.excluir_master, name='excluir_master'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
