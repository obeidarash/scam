from django.db import models
from tinymce.models import HTMLField


class Qa(models.Model):
    question = models.CharField(max_length=256, blank=False, null=False)
    answer = HTMLField()
    created = models.DateTimeField(verbose_name="Date", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Date", auto_now=True, null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question & Answer'
        verbose_name_plural = 'Questions & Answers'


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
