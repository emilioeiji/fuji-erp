from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from cadastro.models import Master


class Tamanho (models.Model):
    tamanho = models.CharField(max_length=10, help_text="Descricao Uniforme")

    def __str__(self):
        return self.tamanho


class Condicao (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao


class StatusSolicitacao (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Uniforme (models.Model):
    descricao = models.CharField(max_length=50, help_text="Descricao Uniforme")
    condicao = models.ForeignKey(Condicao, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.descricao} - {self.condicao} - {self.tamanho} - Valor: {self.valor}"


class Estoque(models.Model):
    uniforme_tamanho = models.ForeignKey(Uniforme, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.uniforme_tamanho.condicao} - {self.uniforme_tamanho.descricao} - {self.uniforme_tamanho.tamanho} - Estoque: {self.quantidade}"


class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(
        'Solicitacao', on_delete=models.CASCADE, related_name='itens')
    uniforme_tamanho = models.ForeignKey(Uniforme, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Solicitação: {self.solicitacao.id_solicitacao} - Uniforme: {self.uniforme_tamanho}"


class Solicitacao(models.Model):
    id_solicitacao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Master, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusSolicitacao, on_delete=models.CASCADE)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id_solicitacao} - Funcionário: {self.funcionario.nomeRomanji}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for item in self.itens.all():
            estoque = Estoque.objects.get(
                uniforme_tamanho=item.uniforme_tamanho)
            estoque.quantidade -= item.quantidade
            estoque.save()


# @receiver(post_save, sender=Solicitacao)
# def deduzir_estoque(sender, instance, **kwargs):
#    estoque = Estoque.objects.get(
#        uniforme_tamanho=instance.uniforme_tamanho)
#    estoque.quantidade -= instance.quantidade
#    estoque.save()
