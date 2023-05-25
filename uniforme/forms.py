from django import forms
from django.forms import inlineformset_factory

from .models import ItemSolicitacao, Solicitacao


class SolicitacaoUniformeForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        # Campos adicionais da solicitação (além do usuário)
        fields = ['funcionario']


ItemSolicitacaoFormSet = inlineformset_factory(
    Solicitacao, ItemSolicitacao, fields=('uniforme', 'tamanho', 'quantidade'), extra=1)
