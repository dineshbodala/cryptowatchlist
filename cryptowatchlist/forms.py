import imp
from traceback import format_stack
from django import forms
from django.forms import ModelForm

from .models import *


class NewCoinForm(forms.ModelForm):
    coin= forms.CharField(label='New Coin')

    class Meta:
        model=Crypto
        fields='__all__'

