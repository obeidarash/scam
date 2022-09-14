from django.shortcuts import render
from .models import  Contact
from core.models import Qa
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def contact(request):
    contact = Contact.objects.all().first()
    context = {
        'contact': contact
    }
    return render(request, 'core/contact.html', context)


def manifest(request):
    qas = Qa.objects.all()
    context = {
        'qas': qas,
    }
    return render(request, 'manifest.html', context)
