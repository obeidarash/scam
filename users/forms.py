from django import forms
from django.core import validators


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': '*****',
            'name': 'password',
            'id': 'password',
            'class': 'form-control'
        }
    ))
