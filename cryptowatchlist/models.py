from django.db import models




class User(models.Model):
    username=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.username

class Crypto(models.Model):
    coins=(('BTC/USDT', 'Bitcoin'), ('ETH','Etherium'), ('SOL', 'Solana'))
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    crypto_name = models.CharField(max_length=100, null=True, choices=coins) 
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.crypto_name



