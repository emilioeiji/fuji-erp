from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('editar_calendario/', views.editar_calendario, name='editar_calendario'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
