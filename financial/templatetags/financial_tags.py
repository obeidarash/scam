from django import template
from ..models import Deposit

register = template.Library()


@register.filter(name='deposit_check')
def deposit_check(user):
    deposit_list = Deposit.objects.filter(user__email=user)
    for deposit in deposit_list:
        if deposit.is_approved:
            return True
    return False
