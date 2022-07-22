from curses.ascii import HT
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


def index(request):
    ct =str(datetime.datetime.now().replace(second=0, microsecond=0))
    exchange = ccxt.binance()
    added_time = int(datetime.datetime.strptime("2022-06-27 09:00:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    current_time=int(datetime.datetime.strptime(ct, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    
    for i in x:
        price_current_time = exchange.fetch_ohlcv(i, '1m',current_time, 1)
        price_added_time = exchange.fetch_ohlcv(i, '1m', added_time, 1)
        total=int(price_added_time[0][4])-int(price_current_time[0][4])
        context={'total':total}
    return render(request, 'cryptowatchlist/index.html', context)

def add_coin(request):
    return render(request, 'cryptowatchlist/add.html')

