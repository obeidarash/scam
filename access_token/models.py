from django.db import models
from users.models import User


class AccessToken(models.Model):
    access_token = models.CharField(max_length=128, verbose_name="Access Token", null=False, blank=False)
    representative = models.ForeignKey(User, on_delete=models.CASCADE,
                                       help_text="That user whom created this after deposit confirm",
                                       related_name='representative_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="user registered with this token", null=True,
                             blank=True)
    is_used = models.BooleanField(default=False, help_text='a user registered with this token')
    by_superuser = models.BooleanField(default=False, verbose_name='Create by admin',
                                       help_text="Super user Created this Accesses token manually")
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)

    def __str__(self):
        return self.access_token
