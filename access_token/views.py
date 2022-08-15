from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import uuid
from access_token.models import AccessToken
from django.contrib import messages


def at(request):
    return render(request, 'at/at.html', context={})


@login_required(login_url='/login')
def at_generator(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        while True:
            uid = str(uuid.uuid4().hex)[:10]
            ac_is_exist = AccessToken.objects.filter(access_token=uid).exists()
            # to avoid create duplicate Accesses Token
            if not ac_is_exist:
                AccessToken.objects.create(access_token=uid, by_superuser=True, representative=request.user)
                messages.success(request, uid)
                redirect('at:at_generator')
                break

    context = {

    }
    return render(request, 'at/at_generator.html', context)
