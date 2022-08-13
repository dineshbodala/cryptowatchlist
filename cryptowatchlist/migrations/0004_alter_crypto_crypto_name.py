# Generated by Django 4.1 on 2022-08-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptowatchlist', '0003_remove_user_coin_crypto_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='crypto_name',
            field=models.CharField(choices=[('BTC/USDT', 'Bitcoin'), ('ETH/USDT', 'Etherium'), ('SOL/USDT', 'Solana')], max_length=100, null=True),
        ),
    ]
