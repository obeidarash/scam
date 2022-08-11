from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import User


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
    if register_form.is_valid():
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        # todo: create 3 token when user is created in another Model
        User.objects.create_user(username=email, email=email, password=password)
        messages.success(request, 'your account has ben created, please log in')
        return redirect('users:login')

    context = {
        'register_form': register_form
    }

    return render(request, 'users/signup.html', context)


def log_out(request):
    logout(request)
    messages.info(request, 'You are out now')
    return redirect('users:login')
