# Generated by Django 4.1 on 2022-08-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
    ]