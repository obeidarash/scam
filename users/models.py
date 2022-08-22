from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# this custom user model made based on this tutorial
# https://www.youtube.com/watch?v=SFarxlTzVX4&list=PLeg9XWX-QxbwLvK8O_xIG6zaCrON-Frjq&index=6


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, fullname=None, country=None, phone_number=None):
        if not email:
            raise ValueError('Users must have an email address.')
        if not username:
            raise ValueError('Users must have an username.')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            fullname=fullname,
            country=country,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    fullname = models.CharField(max_length=30)
    country = CountryField(null=True)
    phone_number = PhoneNumberField(unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
