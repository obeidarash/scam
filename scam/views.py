from django.shortcuts import render, redirect
import uuid


def index(request):
    if not request.user.is_authenticated:
        return redirect('manifest')

    return render(request, 'index.html', context={})


def manifest(request):
    return render(request, 'manifest.html', context={})
