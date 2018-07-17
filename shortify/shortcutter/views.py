from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html')


def short_url(request):
    pass
