from django.shortcuts import render
from .models import Manifest


def manifest(request):
    # todo: add text editor and database for manifest page (Tinymce package)
    mani = Manifest.objects.all().first()
    print(mani)
    context = {
        'mani': mani
    }
    return render(request, 'manifest.html', context)
