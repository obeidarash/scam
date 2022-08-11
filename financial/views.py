from django.shortcuts import render, redirect
from .forms import DepositForm
from .models import Deposit
from django.contrib import messages


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

    # todo: show deposit list to users

    context = {
        'is_deposit_exist_approved': is_deposit_exist_approved,
        'deposit_form': deposit_form
    }
    return render(request, 'financial/deposit.html', context)
