from django.shortcuts import render, redirect
from access_token.models import AccessToken


def index(request):
    if not request.user.is_authenticated:
        return redirect('manifest')

    # show users accesses tokens
    access_tokens = AccessToken.objects.filter(representative=request.user)

    context = {
        'access_tokens': access_tokens
    }
    return render(request, 'index.html', context)


def manifest(request):
    # todo: add text editor and database for manifest page (Tinymce package)
    return render(request, 'manifest.html', context={})
