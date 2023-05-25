from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from cadastro.models import Master


class Tamanho (models.Model):
    tamanho = models.CharField(max_length=10, help_text="Descricao Uniforme")

    def __str__(self):
        return self.tamanho


class Uniforme (models.Model):
    descricao = models.CharField(max_length=50, help_text="Descricao Uniforme")
    valor = models.IntegerField()

    def __str__(self):
        return self.descricao + " - " + str(self.valor)


class Estoque(models.Model):
    uniforme = models.ForeignKey(
        Uniforme, on_delete=models.CASCADE, related_name='estoque')
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['uniforme', 'tamanho']

    def __str__(self):
        return f"Uniforme: {self.uniforme.descricao} - Tamanho: {self.tamanho} - Estoque: {self.quantidade}"


class Solicitacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # Relacionamento com o app "Cadastro.Master"
    funcionario = models.ForeignKey(Master, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação - Funcionário: {self.funcionario.nomeRomanji}"


class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(
        Solicitacao, on_delete=models.CASCADE, related_name='itens')
    uniforme = models.ForeignKey(Uniforme, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Item: {self.uniforme.descricao} - Tamanho: {self.tamanho} - Quantidade: {self.quantidade}"


@receiver(post_save, sender=ItemSolicitacao)
def deduzir_estoque(sender, instance, **kwargs):
    estoque = Estoque.objects.get(
        uniforme=instance.uniforme, tamanho=instance.tamanho)
    estoque.quantidade -= instance.quantidade
    estoque.save()
