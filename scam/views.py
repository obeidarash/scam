from django.shortcuts import render, redirect
import uuid


def index(request):
    if not request.user.is_authenticated:
        return redirect('manifest')

    # todo: test of token generator
    # token app model: token, user
    for _ in range(3):
        uid = str(uuid.uuid4().hex)[:10]
        print(uid)

    return render(request, 'index.html', context={})


def manifest(request):
    return render(request, 'manifest.html', context={})
