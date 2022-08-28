from django.shortcuts import render
from .models import Manifest, Contact


def contact(request):
    contact = Contact.objects.all().first()
    context = {
        'contact': contact
    }
    return render(request, 'core/contact.html', context)


def manifest(request):
    # todo: if login show account link, home and .... to user
    # todo: if not login how login, register, at_list link .... to user
    mani = Manifest.objects.all().first()
    context = {
        'mani': mani
    }
    return render(request, 'manifest.html', context)
