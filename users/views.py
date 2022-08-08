from django.shortcuts import render, HttpResponse


def manifest(request):
    return HttpResponse("OK!")
