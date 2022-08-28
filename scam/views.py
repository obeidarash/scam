from django.shortcuts import render, redirect
from access_token.models import AccessToken
from financial.models import Deposit
from django.contrib.auth.decorators import login_required


# todo: don't show accesses tokens if deposit of user isn't approve
# todo: show users AT, if has any
# todo: if deposit of user isn't true show guid what to do
# todo: if deposit and all 3 users are ok show withdraw request

@login_required(login_url='/login')
def index(request):
    access_tokens = AccessToken.objects.filter(representative=request.user, by_superuser=False)
    is_deposit_exist_approved = Deposit.objects.check_deposit(request.user)
    check_deposit_3_users = Deposit.objects.check_deposit_3_users(request.user)



    context = {
        'access_tokens': access_tokens,
        'is_deposit_exist_approved': is_deposit_exist_approved,
        'check_deposit_3_users': check_deposit_3_users,
    }
    return render(request, 'index.html', context)
