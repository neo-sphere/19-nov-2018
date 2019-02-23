from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import Transaction


class CustomUserCreationForm(UserCreationForm):
    mobile = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ('username', 'email', 'mobile')

class TransactionForm(forms.ModelForm):
    to_mobile = forms.CharField(max_length=15)
    
    class Meta:
        model = Transaction
        fields = ['to_mobile', 'ammount']

    