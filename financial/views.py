from django.shortcuts import render, redirect
from .forms import DepositForm
from .models import Deposit
from access_token.models import AccessToken
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def withdraw(request):
    # todo: if three of users deposit is okay, representative can submit for withdraw
    access_tokens = AccessToken.objects.filter(representative=request.user)

    context = {}
    return render(request, 'financial/withdraw.html', context)


@login_required(login_url='/login')
def deposit(request):
    deposit_form = DepositForm(request.POST or None)
    is_deposit_exist_approved = Deposit.objects.is_deposit_exist_approved(request.user)

    if request.method == "POST":
        if not is_deposit_exist_approved:
            if deposit_form.is_valid():
                hash_id = deposit_form.cleaned_data['hash']
                Deposit.objects.create(user=request.user, hash=hash_id)
                messages.success(request, 'Transfer has been submitted')
                return redirect('financial:deposit')

    # show deposit list to users
    deposit_exist = Deposit.objects.filter(user__email=request.user).exists()
    deposit_list = Deposit.objects.filter(user__email=request.user)

    context = {
        'is_deposit_exist_approved': is_deposit_exist_approved,
        'deposit_form': deposit_form,
        'deposit_exist': deposit_exist,
        'deposit_list': deposit_list,
    }
    return render(request, 'financial/deposit.html', context)
