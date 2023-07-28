from django import template

from space.models import Mensagem

register = template.Library()


@register.filter
def is_lida_by_user(mensagem, user):
    return mensagem.is_lida_by_user(user)
