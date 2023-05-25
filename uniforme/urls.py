from django.urls import path

from . import views

urlpatterns = [
    path('solicitar/', views.solicitar_uniformes, name='solicitar_uniformes'),
]
