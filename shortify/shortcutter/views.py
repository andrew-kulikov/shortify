from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    context = {}

    if request.method == 'GET':
        if 'url' in request.GET:
            url = request.GET['url']
            url = request.META['HTTP_HOST'] + '/ok228'
            messages.info(request, 'Your short url: {}'.format(url), extra_tags='alert-success')

    return render(request, 'base.html', context)


def short_url(request):
    pass
