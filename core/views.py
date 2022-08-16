from django.shortcuts import render
from .models import Manifest


def manifest(request):
    mani = Manifest.objects.all().first()
    context = {
        'mani': mani
    }
    return render(request, 'manifest.html', context)
