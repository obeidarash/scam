from django.db import models
from tinymce.models import HTMLField


class Contact(models.Model):
    title = models.CharField(max_length=512)
    content = HTMLField()

    def __str__(self):
        return self.title


class Manifest(models.Model):
    title = models.CharField(max_length=512)
    content = HTMLField()

    def __str__(self):
        return self.title
