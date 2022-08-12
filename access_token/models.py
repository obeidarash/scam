from django.db import models
from users.models import User


class AccessToken(models.Model):
    access_token = models.CharField(max_length=128, verbose_name="Access Token", null=False, blank=False)
    representative = models.ForeignKey(User, on_delete=models.CASCADE,
                                       help_text="every user has 3 of this code as representative",
                                       related_name='representative_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="belongs to 3 different user", null=True,
                             blank=True)
    is_used = models.BooleanField(default=False)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)

    def __str__(self):
        return self.access_token
