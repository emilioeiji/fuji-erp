from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('master/', views.cadastro_master, name='cadastro_master'),
    path('master_apto/', views.cadastro_master_apto, name='cadastro_master_apto'),
    path('listar_mt', views.listar_mt, name='listar_mt'),
    path('listar_mt_apto', views.listar_mt_apto, name='listar_mt_apto'),
    path('editar-master/<int:codigo_empregado>/',
         views.editar_master, name='editar_master'),
    path('editar-master-apto/<int:numero_apto>/',
         views.editar_master_apto, name='editar_master_apto'),
    path('excluir-master/<int:codigo_empregado>/',
         views.excluir_master, name='excluir_master'),
    path('excluir-master-apto/<int:numero_apto>/',
         views.excluir_master_apto, name='excluir_master_apto'),
    path('detalhar-mt-apto/<int:numero_apto>/', views.detalhar_mt_apto,
         name='detalhar_mt_apto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
