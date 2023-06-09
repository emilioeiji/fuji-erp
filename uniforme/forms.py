from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from cadastro.models import Master

from .models import ItemSolicitacao, Solicitacao


class SolicitacaoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['funcionario'].required = True
        self.fields['status'].required = True

        class Meta:
            model = Solicitacao
            fields = ['usuario', 'funcionario', 'status']
            labels = {
                'usuario': 'Nome do usuário',
                'funcionario': 'Nome do funcionário',
                'status': 'Status da solicitação',
            }

            widgets = {
                'usuario': forms.TextInput(attrs={'class': 'form-control'}),
                'funcionario': forms.TextInput(attrs={'class': 'form-control'}),
                'status': forms.TextInput(attrs={'class': 'form-control'}),
            }


class ItemSolicitacaoform(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uniforme_tamanho'].required = True
        self.fields['quantidade'].required = True

        class Meta:
            model = ItemSolicitacao
            fields = ['uniforme_tamanho', 'quantidade']
            labels = {
                'uniforme_tamanho': 'Modelo uniforme',
                'quantidade': 'Quantidade',
            }

            widgets = {
                'uniforme_tamanho': forms.TextInput(attrs={'class': 'form-control'}),
                'quantidade': forms.TextInput(attrs={'class': 'form-control'})
            }
