from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import User
import uuid
from access_token.models import AccessToken


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    login_form = LoginForm(request.POST or None)

    if request.method == "POST":
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'your are login')
                return redirect('home')
            else:
                messages.error(request, 'Email or Password is wrong')
                redirect('users:login')

    context = {
        'login_form': login_form
    }
    return render(request, 'users/login.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    register_form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if register_form.is_valid():
            # todo: fix problem with clean password validator
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            access_token = register_form.cleaned_data.get('access_token')
            User.objects.create_user(username=email, email=email, password=password)

            #  login user after registration
            user = authenticate(request, email=email, password=password)
            login(request, user)

            # burn accesses token that user used to register
            access_token_find = AccessToken.objects.get(access_token=access_token)
            access_token_find.user = request.user
            access_token_find.is_used = True
            access_token_find.save()

            # create 3 token when user is created in another Model
            for _ in range(3):
                uid = str(uuid.uuid4().hex)[:10]
                AccessToken.objects.create(representative=request.user, access_token=uid)

            messages.success(request, 'your are login')
            return redirect('home')

    context = {
        'register_form': register_form
    }

    return render(request, 'users/signup.html', context)


def log_out(request):
    logout(request)
    messages.info(request, 'You are out now')
    return redirect('users:login')
