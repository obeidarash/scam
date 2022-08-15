from django import forms
from users.models import User
from django.core import validators
from access_token.models import AccessToken


class ProfileForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control'
        }
    ))


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

    # todo: validate user email and password in here


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control'
        }
    ))

    access_token = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': '465fh688s679',
            'name': 'access_token',
            'id': 'access_token',
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
    ))

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
            raise forms.ValidationError("Passwords does not match")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=username).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('This username exist')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_email_by_email = User.objects.filter(email=email).exists()
        if is_exists_email_by_email:
            raise forms.ValidationError('This email exist')
        return email

    # check for valid token
    def clean_access_token(self):
        access_token = self.cleaned_data.get('access_token')
        access_token_is_valid = AccessToken.objects.filter(access_token=access_token, is_used=False).exists()
        if not access_token_is_valid:
            raise forms.ValidationError('this token is not valid')
        return access_token
