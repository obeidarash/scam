from django.shortcuts import render, redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect('manifest')

    return render(request, 'index.html', context={})


def manifest(request):
    if request.user.is_authenticated:
        return redirect('manifest')
    return render(request, 'manifest.html', context={})
