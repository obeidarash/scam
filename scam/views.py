from django.shortcuts import render, redirect
from access_token.models import AccessToken
from financial.models import Deposit


def index(request):
    # show users accesses tokens
    # don't show accesses tokens if deposit of user isn't approve
    access_tokens = AccessToken.objects.filter(representative=request.user, by_superuser=False)
    is_deposit_exist_approved = Deposit.objects.is_deposit_exist_approved(request.user)

    context = {
        'access_tokens': access_tokens,
        'is_deposit_exist_approved': is_deposit_exist_approved,
    }
    return render(request, 'index.html', context)
