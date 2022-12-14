from django import forms
from users.models import User
from django.core import validators
from access_token.models import AccessToken
from django_countries.fields import CountryField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox, ReCaptchaV3


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Search for a user',
            'name': 'search',
            'id': 'search',
            'class': 'form-control',
            'autofocus': 'True'
        }
    ))


class LoginForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control',
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': '**********',
            'name': 'password',
            'id': 'password',
            'class': 'form-control'
        }
    ))


class RegisterForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    country = CountryField(blank=False).formfield()

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control',
        }
    ))

    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Benjamin Bottom',
            'name': 'fullname',
            'id': 'fullname',
            'class': 'form-control'
        }
    ), validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(25)])

    access_token = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': '465fh688s679',
            'name': 'access_token',
            'id': 'access_token',
            'class': 'form-control',
            'label': 'Token'
        }
    ))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'placeholder': '**********',
            'name': 'password',
            'id': 'password',
            'class': 'form-control'
        }
    ), validators=[validators.MinLengthValidator(6), validators.MaxLengthValidator(20)])
    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': '**********',
            'name': 're_password',
            'id': 're_password',
            'class': 'form-control'
        }
    ), validators=[validators.MinLengthValidator(6), validators.MaxLengthValidator(20)])

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
            raise forms.ValidationError("This email exist, <a href='login'>login here</a>")
        return email

    # check for valid token
    def clean_access_token(self):
        access_token = self.cleaned_data.get('access_token')
        access_token_is_valid = AccessToken.objects.filter(access_token=access_token, is_used=False).exists()
        if not access_token_is_valid:
            raise forms.ValidationError(
                "this token is not valid, if you don't have any token check <a href='at:at'>this page</a>")
        return access_token


class ProfileForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com',
            'name': 'email',
            'id': 'email',
            'class': 'form-control',

        }
    ), disabled=True)

    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Brad Pit',
            'name': 'fullname',
            'id': 'fullname',
            'class': 'form-control'
        }
    ), validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(25), ], disabled=True)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': '**********',
            'name': 'password',
            'id': 'password',
            'class': 'form-control'
        }
    ), disabled=True, required=False)
