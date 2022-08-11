from django import forms
from .models import Deposit
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


class DepositAdminForm(forms.ModelForm):
    class Meta:
        model: Deposit
        fields: '__all__'

    def clean(self):
        if self.cleaned_data['is_approved'] and self.cleaned_data['is_decline']:
            raise forms.ValidationError("is approved and is decline can't be true in the same time!")
