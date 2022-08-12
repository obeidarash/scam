from django.db import models
from users.models import User


class DepositManager(models.Manager):

    # check deposit status (paid or not paid!)
    def is_deposit_exist_approved(self, user):
        deposit_list = Deposit.objects.filter(user__email=user)
        for deposit in deposit_list:
            if not deposit.is_approved and not deposit.is_decline:
                return True
            if deposit.is_approved:
                return True
        return False


# with this model user can charge his account
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    hash = models.CharField(max_length=1000, verbose_name='Transaction HASH or TXID', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_decline = models.BooleanField(default=False)

    objects = DepositManager()

    def __str__(self):
        return self.user.email


# with this model user can request for withdraw
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    is_approved = models.BooleanField(default=False, help_text='Everything is ok for payment')
    is_payed = models.BooleanField(default=False, help_text='Money transfer is done')
    wallet_id = models.CharField(max_length=1000, verbose_name='Wallet Address', null=False, blank=False)
    # todo: add validator to admin - if is_payed is true hash cant be empty
    hash = models.CharField(max_length=1000, verbose_name='Transaction HASH or TXID', null=True, blank=True)

    def __str__(self):
        return self.user.email
