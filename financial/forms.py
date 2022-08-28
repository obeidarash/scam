from django import forms
from .models import Deposit, Withdraw
from users.models import User


class WithdrawForm(forms.Form):
    wallet_id = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': '',
            'name': 'wallet_id',
            'id': 'wallet_id',
            'class': 'form-control',
        }
    ))


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

    def clean_hash(self):
        deposit = Deposit.objects.filter(hash__exact=self.cleaned_data['hash']).exists()
        if deposit:
            raise forms.ValidationError('This HASH or TXID already exists!')
        return self.cleaned_data['hash']


class WithdrawAdminForm(forms.ModelForm):
    class Meta:
        model: Withdraw
        fields: '__all__'

    def clean(self):
        if self.cleaned_data['is_approved'] and self.cleaned_data['hash'] is None:
            raise forms.ValidationError("if is paid is True, hash cant be empty")
        if not self.cleaned_data['is_approved'] and self.cleaned_data['hash'] is not None:
            raise forms.ValidationError("if is paid is False, hash cant be filled")


class DepositAdminForm(forms.ModelForm):
    class Meta:
        model: Deposit
        fields: '__all__'

    def clean(self):
        if self.cleaned_data['is_approved'] and self.cleaned_data['is_decline']:
            raise forms.ValidationError("is approved and is decline can't be true in the same time!")
