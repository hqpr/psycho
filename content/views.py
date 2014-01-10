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
    m = Navigation.objects.all()
    data = {'p': p, 'm': m}
    return render(request, 'pages.html', data)


# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
# http://djbook.ru/rel1.4/howto/custom-template-tags.html