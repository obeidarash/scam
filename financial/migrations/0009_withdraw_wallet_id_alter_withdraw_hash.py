# Generated by Django 4.1 on 2022-08-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0008_deposit_is_decline'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='wallet_id',
            field=models.CharField(default=0, max_length=1000, verbose_name='Wallet Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='hash',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Transaction HASH or TXID'),
        ),
    ]