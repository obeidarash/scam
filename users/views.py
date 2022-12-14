from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, ProfileForm, SearchForm
from django.contrib import messages
from .models import User
import uuid
from access_token.models import AccessToken
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import JsonResponse
from django.db.models import Q
import json
from django.http import HttpResponse


# return specific user
@login_required(login_url='/login')
def find_user(request):
    return HttpResponse('hello')


# return search page
@login_required(login_url='/login')
def search(request):
    if not request.user.is_superuser:
        return redirect('home')

    search_form = SearchForm(request.POST or None)

    context = {
        'search_form': search_form,
    }
    return render(request, 'users/search.html', context)


# return data of search form
@login_required(login_url='/login')
def search_query(request):
    if not request.user.is_superuser:
        return redirect('home')

    search = request.GET['search']
    users = User.objects.filter(
        Q(fullname__icontains=search) | Q(email__exact=search) | Q(username__exact=search))
    print(users)
    return JsonResponse({
        'users': list(users.values())
    }, safe=False)


@login_required(login_url='/login')
def profile(request):
    profile_form = ProfileForm(request.POST or None, initial={'email': request.user.email,
                                                              'fullname': request.user.fullname})
    if request.method == "POST":
        if profile_form.is_valid():
            pass

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)


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
                # Return to Admin area if user is admin
                if request.user.is_superuser:
                    return redirect('/thisispanelarea')
                messages.success(request, ' Wellcome')
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

    # Validate register form
    register_form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if register_form.is_valid():

            # Fetch form data
            email = register_form.cleaned_data.get('email')
            phone_number = register_form.cleaned_data.get('phone_number')
            country = register_form.cleaned_data.get('country')
            password = register_form.cleaned_data.get('password')
            fullname = register_form.cleaned_data.get('fullname')
            access_token = register_form.cleaned_data.get('access_token')
            User.objects.create_user(username=email, email=email, password=password, fullname=fullname, country=country,
                                     phone_number=phone_number)

            #  login user after registration
            user = authenticate(request, email=email, password=password)
            login(request, user)

            # burn accesses token that user used to register
            access_token_find = AccessToken.objects.get(access_token=access_token)
            access_token_find.user = request.user
            access_token_find.is_used = True
            access_token_find.save()

            # create 3 token when user is created and avoid create duplicate token
            counter = 1
            while counter <= 3:
                uid = str(uuid.uuid4().hex)[:10]
                ac_is_exist = AccessToken.objects.filter(access_token=uid).exists()
                if not ac_is_exist:
                    print('ok')
                    AccessToken.objects.create(representative=request.user, access_token=uid, by_superuser=False)
                    counter += 1

            messages.success(request, 'your are login')
            return redirect('home')

    context = {
        'register_form': register_form
    }

    return render(request, 'users/signup.html', context)


@login_required(login_url='/login')
def log_out(request):
    logout(request)
    messages.info(request, ' See you soon')
    return redirect('users:login')
