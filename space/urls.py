from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.space, name='space'),
    path('lista-space/<int:space_id>/', views.lista_space, name='lista_space'),
    path('lista-mensagens/<int:space_id>/',
         views.lista_mensagens, name='lista_mensagens'),
    path('lista-tema/<int:tema_id>/', views.lista_tema, name='lista_tema'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
