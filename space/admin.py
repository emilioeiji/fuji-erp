from django.contrib import admin

from space import models

admin.site.register(models.Space)
admin.site.register(models.Tema)
admin.site.register(models.Topico)
admin.site.register(models.Mensagem)
admin.site.register(models.LeituraMensagem)
