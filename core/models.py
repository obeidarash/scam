from django.db import models
from tinymce.models import HTMLField


class Qa(models.Model):
    question = models.CharField(max_length=256, blank=False, null=False)
    answer = HTMLField()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(verbose_name="Create", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Edit", auto_now=True, null=True)

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


class Tag(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    created = models.DateTimeField(verbose_name="Create", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Edit", auto_now=True, null=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=64, unique=True)
    content = HTMLField()
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=128, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(verbose_name="Create", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Edit", auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
