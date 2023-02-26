from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('master/', views.cadastro_master, name='cadastro_master'),
]
