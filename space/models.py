from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from cadastro.models import Area


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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, null=True)
    data_hora_criacao = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['tema', 'topico']

    def __str__(self):
        return f"{self.tema.nome} - {self.topico}"


class Mensagem(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = RichTextField()
    mensagem_original = models.ForeignKey(
        'self', null=True, blank=True, related_name='respostas', on_delete=models.CASCADE)
    data_hora_criacao = models.DateTimeField(default=timezone.now)
    data_hora_resposta = models.DateTimeField(default=timezone.now)

    def is_lida_by_user(self, user):
        return self.leituramensagem_set.filter(usuario=user, lida=True).exists()

    def __str__(self):
        return self.mensagem


@receiver(post_save, sender=Mensagem)
def criar_leitura_mensagem(sender, instance, created, **kwargs):
    if created:
        usuarios = User.objects.filter(
            Q(perfil__area=instance.topico.tema.space.area.area) | Q(
                id=instance.usuario_id)
        )

        for usuario in usuarios:
            # Verifica se o usuário é o mesmo que criou a mensagem
            lida = usuario == instance.usuario
            LeituraMensagem.objects.create(
                mensagem=instance, usuario=usuario, lida=lida)


class LeituraMensagem(models.Model):
    mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"Leitura da mensagem {self.mensagem_id} pelo usuário {self.usuario_id}"
