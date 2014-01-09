# -- coding: utf-8 --
#!/usr/bin/env python

from .models import Pages, Navigation
from django.shortcuts import render

def index(request):
    p = Pages.objects.get(slug='index')
    data = {'p': p}
    return render(request, 'index.html', data)


def pages(request, slug):
    p = Pages.objects.get(slug=slug)
    data = {'p': p}
    return render(request, 'pages.html', data)


def menu(request):
    m = Navigation.objects.all()
    data = {'m': m}
    return render(request, 'inc/menu.html', data)
# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/