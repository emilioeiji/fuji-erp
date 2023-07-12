from django.db import models

from cadastro.models import Area, Master


class Space(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Space")

    class Meta:
        ordering = ['area']
        constraints = [
            models.UniqueConstraint(
                fields=['area', 'nome'], name='unique_space_combination'
            )
        ]

    def __str__(self):
        return f"{self.area} - {self.nome}"


class Tema(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, help_text="Nome do Tema")

    class Meta:
        ordering = ['space', 'nome']

    def __str__(self):
        return f"{self.space} - {self.nome}"


class Topico(models.Model):
    topico = models.CharField(max_length=100, help_text="Nome do Tema")
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['tema', 'topico']

    def __str__(self):
        return f"{self.tema.nome} - {self.topico}"
