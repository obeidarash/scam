from django.shortcuts import render, redirect
import uuid


def index(request):
    # todo: work on token generator and its model
    for _ in range(3):
        uid = str(uuid.uuid4().hex)[:10]
        print(uid)

    if not request.user.is_authenticated:
        return redirect('manifest')

    return render(request, 'index.html', context={})


def manifest(request):
    return render(request, 'manifest.html', context={})
