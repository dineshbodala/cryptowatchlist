from datetime import datetime
from multiprocessing import context
from operator import index
import re
from django.shortcuts import render
from django.http import HttpResponse
import ccxt
from datetime import datetime
import cryptowatchlist
import datetime
from django.http import HttpResponseRedirect
from django.forms import Form
from django import forms 
from django.shortcuts import render
from django.urls import reverse
from . import forms
from .models import Crypto, User
exchange = ccxt.binance()

def index(request):
    users=User.objects.get(id=3)
    y=[]
    c=0
    coins=users.crypto_set.all()
    ct = str(datetime.datetime.now().replace(second=0, microsecond=0))
    for i in coins:
        added_time = str(i.added_time.replace(second=0, microsecond=0))
        added_time=added_time[:19]
        c_added_time=int(datetime.datetime.strptime(added_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        current_time = int(datetime.datetime.strptime(ct, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        price_current_time = exchange.fetch_ohlcv(i.crypto_name+'/USDT', '1m', current_time, 1)
        price_added_time = exchange.fetch_ohlcv(i.crypto_name+'/USDT', '1m', c_added_time, 1)
        total = int(price_added_time[0][4]) - int(price_current_time[0][4])
        y.append(total)

    context={'coins':coins, 'y':y}
    return render(request, 'cryptowatchlist/index.html', context)


def add_coin(request):    
    return render(request, 'cryptowatchlist/add.html')


    

