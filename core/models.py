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

    class Meta:
        verbose_name_plural = 'Contact'


class Tag(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    created = models.DateTimeField(verbose_name="Create", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Edit", auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtags'


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    created = models.DateTimeField(verbose_name="Create", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Edit", auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    content = HTMLField()
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='Hashtags', help_text='You can pick more than one')
    category = models.ForeignKey(Category, help_text='You pick only 1 category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=128, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(verbose_name="Create", auto_now_add=True, null=True)
    edited = models.DateTimeField(verbose_name="Edit", auto_now=True, null=True)

    def __str__(self):
        return self.title
