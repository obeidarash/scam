# Generated by Django 4.1 on 2022-08-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_qa_options_qa_created_qa_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='qa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create'),
        ),
        migrations.AlterField(
            model_name='qa',
            name='edited',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Edit'),
        ),
    ]
