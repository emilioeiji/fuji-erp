from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    foto_perfil = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario.username
