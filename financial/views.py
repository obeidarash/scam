from django.shortcuts import render, redirect
from .forms import DepositForm
from .models import Deposit
from django.contrib import messages


def deposit(request):
    deposit_form = DepositForm(request.POST or None)

    if request.method == "POST":
        if deposit_form.is_valid():
            hash_id = deposit_form.cleaned_data['hash']
            Deposit.objects.create(user=request.user, hash=hash_id)
            messages.success(request, 'Transfer has been submitted')
            return redirect('financial:deposit')

    # todo: do not show deposit from to the user if there is any submitted deposit
    # todo: show deposit form if there is declined form in database

    context = {
        'deposit_form': deposit_form
    }
    return render(request, 'financial/deposit.html', context)
