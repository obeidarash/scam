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


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'placeholder': '*****',
            'name': 'password',
            'id': 'password',
            'class': 'form-control'
        }
    ))
    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': '*****',
            'name': 're_password',
            'id': 're_password',
            'class': 'form-control'
        }
    ), required=True)

    # phone = forms.CharField(widget=forms.NumberInput(
    #     attrs={
    #         'placeholder': '+1354898769',
    #         'name': 'phone',
    #         'id': 'phone',
    #         'class': 'form-control'
    #     }
    # ))

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('Passwords Doesnt match')
        return password
