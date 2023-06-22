from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('master/', views.cadastro_master, name='cadastro_master'),
    path('listar_mt', views.listar_mt, name='listar_mt'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
