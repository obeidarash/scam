from django.db import models
from users.models import User
from access_token.models import AccessToken


class WithdrawManager(models.Manager):

    # to prevent user send multiple withdraw request
    def is_withdraw_exist_approved(self, user):
        withdraw_list = Withdraw.objects.filter(user__email=user)
        for withdraw in withdraw_list:
            if not withdraw.is_approved and not withdraw.is_decline:
                return True
            if withdraw.is_approved:
                return True
        return False

    def is_withdraw_approved(self, user):
        withdraw_list = Withdraw.objects.filter(user__email=user)
        for withdraw in withdraw_list:
            if withdraw.is_approved:
                return True
        return False

    # return hash of approved withdraw
    def withdraw_approved_hash(self, user):
        withdraw_list = Withdraw.objects.filter(user__email=user)
        for withdraw in withdraw_list:
            if withdraw.is_approved:
                return withdraw.hash
        return False


class DepositManager(models.Manager):

    # check deposit status (paid or not paid!); just can be used in deposit view
    def is_deposit_exist_approved(self, user):
        deposit_list = Deposit.objects.filter(user__email=user)
        for deposit in deposit_list:
            if not deposit.is_approved and not deposit.is_decline:
                return True
            if deposit.is_approved:
                return True
        return False

    def check_deposit(self, user):
        deposit_list = Deposit.objects.filter(user__email=user)
        for deposit in deposit_list:
            if deposit.is_approved:
                return True
        return False

    # this function has not been used, and it's not working correctly
    def check_deposit_3_users(self, user):
        # fetch deposit of all 3 user based on tokens
        ats = AccessToken.objects.filter(representative=user)
        for at in ats:
            deposits = Deposit.objects.filter(user__email=at.user)
            if len(deposits) > 1:
                deposit_status = []
                for deposit in deposits:
                    deposit_status.append(deposit.is_approved)
                if True not in deposit_status:
                    return False
            else:
                for deposit in deposits:
                    if not deposit.is_approved:
                        return False
        return True


# with this model user can charge his account
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    hash = models.CharField(max_length=1000, verbose_name='Transaction HASH or TXID', null=True, blank=True,
                            unique=True)
    is_approved = models.BooleanField(default=False)
    is_decline = models.BooleanField(default=False)

    objects = DepositManager()

    def __str__(self):
        return self.user.email


# with this model user can request for withdraw
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    is_decline = models.BooleanField(default=False, help_text='cant pay')

    is_approved = models.BooleanField(default=False, help_text='Everything is ok and payed')
    wallet_id = models.CharField(max_length=1000, verbose_name='Wallet Address', null=False, blank=False,
                                 help_text='Wallet ID of user')
    hash = models.CharField(max_length=1000, verbose_name='Transaction HASH or TXID', null=True, blank=True,
                            help_text='ID of transaction of money to the user')
    objects = WithdrawManager()

    def __str__(self):
        return self.user.email
