# -- coding: utf-8 --
#!/usr/bin/env python

from .models import Pages, Navigation, ContactForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect


def index(request):
    p = Pages.objects.get(slug='index')
    data = {'p': p}
    return render(request, 'index.html', data)


def pages(request, slug):
    p = Pages.objects.get(slug=slug)
    m = Navigation.objects.order_by('position')
    data = {'p': p, 'm': m}
    return render(request, 'pages.html', data)


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['layzfromlp@gmail.com']
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/page/thanks/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })



# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
# http://djbook.ru/rel1.4/howto/custom-template-tags.html