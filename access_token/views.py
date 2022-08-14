from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import uuid
from access_token.models import AccessToken
from django.contrib import messages


def ac(request):
    return render(request, 'ac/ac.html', context={})


@login_required(login_url='/login')
def ac_generator(request):
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
                redirect('ac:ac_generator')
                break

    context = {

    }
    return render(request, 'ac/ac_generator.html', context)
