from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages


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
    return render(request, 'users/signup.html', context={})


def log_out(request):
    logout(request)
    messages.info(request, 'You are out now')
    return redirect('users:login')
