from django.db import models
from users.models import User
from datetime import datetime


# with this model user can charge his account
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    hash = models.CharField(max_length=1000, verbose_name='Transaction HASH or TXID', null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


# with this model user can request for withdraw
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    is_approved = models.BooleanField(default=False, help_text='Everything is ok for payment')
    is_payed = models.BooleanField(default=False, help_text='Money transfer is done')
    hash = models.TextField(max_length=10000, verbose_name='Transaction HASH or TXID')

    def __str__(self):
        return self.user.email
