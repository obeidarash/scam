from django.shortcuts import render, redirect
from .forms import DepositForm, WithdrawForm
from .models import Deposit, Withdraw
from access_token.models import AccessToken
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def withdraw(request):
    is_withdraw_ok = False

    # Check representative Deposit Status
    if Deposit.objects.check_deposit(request.user):
        # check if all three user are registered
        users_status = AccessToken.objects.check_user_status(request.user)
        if users_status:
            # Check if all 3 users deposit status is okay
            access_tokens = AccessToken.objects.filter(representative=request.user)
            for access_token in access_tokens:
                access_token_user = Deposit.objects.check_deposit(access_token.user)
                if not access_token_user:
                    is_withdraw_ok = False
                    break
                is_withdraw_ok = True

    withdraw_approved_hash = Withdraw.objects.withdraw_approved_hash(request.user)
    is_withdraw_approved = Withdraw.objects.is_withdraw_approved(request.user)
    withdraw_form = WithdrawForm(request.POST or None)
    if request.method == "POST" and is_withdraw_ok:
        if withdraw_form.is_valid():
            wallet_id = withdraw_form.cleaned_data['wallet_id']
            Withdraw.objects.create(user=request.user, wallet_id=wallet_id)
            messages.success(request, 'Withdraw request has been sent')
            return redirect('financial:withdraw')

    # check withdraw status to prevent user send multiple request
    is_withdraw_exist_approved = Withdraw.objects.is_withdraw_exist_approved(request.user)

    # get list of withdraws
    withdraw_list = Withdraw.objects.filter(user=request.user)

    context = {
        'is_withdraw_ok': is_withdraw_ok,
        'withdraw_form': withdraw_form,
        'is_withdraw_exist_approved': is_withdraw_exist_approved,
        'withdraw_list': withdraw_list,
        'is_withdraw_approved': is_withdraw_approved,
        'withdraw_approved_hash': withdraw_approved_hash,
    }

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
    deposit_is_approved = Deposit.objects.check_deposit(request.user)
    deposit_exist = Deposit.objects.filter(user__email=request.user).exists()
    deposit_list = Deposit.objects.filter(user__email=request.user)

    context = {
        'is_deposit_exist_approved': is_deposit_exist_approved,
        'deposit_form': deposit_form,
        'deposit_exist': deposit_exist,
        'deposit_list': deposit_list,
        'deposit_is_approved': deposit_is_approved,
    }
    return render(request, 'financial/deposit.html', context)
