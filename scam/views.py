from django.shortcuts import render, redirect
from access_token.models import AccessToken
from financial.models import Deposit, Withdraw
from django.contrib.auth.decorators import login_required


# don't show accesses tokens if deposit of user isn't approve
# show users AT, if has any
# if deposit of user isn't true show guid what to do
# if deposit and all 3 users are ok show withdraw request
# if withdraw is true show message

@login_required(login_url='/login')
def index(request):
    access_tokens = AccessToken.objects.filter(representative=request.user, by_superuser=False)
    is_deposit_exist_approved = Deposit.objects.check_deposit(request.user)
    check_deposit_3_users = Deposit.objects.check_deposit_3_users(request.user)
    is_withdraw_approved = Withdraw.objects.is_withdraw_approved(request.user)
    withdraw_approved_hash = Withdraw.objects.withdraw_approved_hash(request.user)

    context = {
        'access_tokens': access_tokens,
        'is_deposit_exist_approved': is_deposit_exist_approved,
        'check_deposit_3_users': check_deposit_3_users,
        'is_withdraw_approved': is_withdraw_approved,
        'withdraw_approved_hash': withdraw_approved_hash,
    }
    return render(request, 'index.html', context)
