from django import forms
from users.models import User


class DepositForm(forms.Form):
    hash = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Input HASH or TXID in this box',
            'name': 'hash',
            'id': 'hash',
            'class': 'form-control',
            'aria-describedby': 'hash-help',
        }
    ))
