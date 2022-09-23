from django.db import models
from users.models import User


class AccessTokenManager(models.Manager):

    # check if all three user are registered
    def check_user_status(self, user):
        access_tokens = AccessToken.objects.filter(representative=user)
        for at in access_tokens:
            if at.user is None:
                return False
        return True


class AccessToken(models.Model):
    access_token = models.CharField(max_length=128, verbose_name="Access Token", null=False, blank=False,
                                    help_text='unique number who belongs to one person')
    representative = models.ForeignKey(User, on_delete=models.CASCADE,
                                       help_text="That user whom created this after deposit confirm",
                                       related_name='representative_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="user registered with this token", null=True,
                             blank=True)
    is_used = models.BooleanField(default=False, help_text='user used this token to register')
    by_superuser = models.BooleanField(default=False, verbose_name='Create by admin',
                                       help_text="Admin (superuser) Created this token manually")
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    objects = AccessTokenManager()

    def __str__(self):
        return self.access_token
