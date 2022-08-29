# Generated by Django 4.1 on 2022-08-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_qa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qa',
            options={'verbose_name': 'Question & Answer', 'verbose_name_plural': 'Questions & Answers'},
        ),
        migrations.AddField(
            model_name='qa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='qa',
            name='edited',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date'),
        ),
    ]
