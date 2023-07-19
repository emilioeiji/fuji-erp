from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.space, name='space'),
    path('lista-mensagens/<int:space_id>/',
         views.lista_mensagens, name='lista_mensagens'),
    path('conteudo-topico/<int:space_id>/<int:tema_id>/',
         views.conteudo_topico, name='conteudo_topico'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
