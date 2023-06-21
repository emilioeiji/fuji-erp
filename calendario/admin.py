from django.contrib import admin

from calendario import models

admin.site.register(models.Calendario)
admin.site.register(models.DiaCalendario)
admin.site.register(models.Alocacao)
admin.site.register(models.FuncionarioCalendario)
