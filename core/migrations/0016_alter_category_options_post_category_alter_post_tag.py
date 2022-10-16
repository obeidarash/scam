# Generated by Django 4.1.1 on 2022-10-15 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_category_alter_post_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, help_text='You pick only 1 category', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='You can pick more than one', to='core.tag', verbose_name='Hashtags'),
        ),
    ]
