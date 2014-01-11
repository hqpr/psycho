# -*- coding: utf-8 -*-
from django.db import models
from django import forms


class Pages(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название страницы')
    title = models.CharField(max_length=100, verbose_name='Заголовок страницы', help_text='TITLE', blank=True)
    slug = models.CharField(max_length=100, verbose_name='URL')
    text = models.TextField(verbose_name='Текст страницы')
    description = models.TextField(verbose_name='Описание страницы', blank=True, null=True, help_text='Не обязательно')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'страницы'

    def __unicode__(self):
        return self.name


class Navigation(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название пункта')
    slug = models.CharField(max_length=100, verbose_name='URL')
    position = models.IntegerField(verbose_name=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Навигация'
        verbose_name_plural = 'навигация'

    def __unicode__(self):
        return self.name


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
