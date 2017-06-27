# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from homepage.models import Tattoo

# Create your views here.
def home(request):
    tattoo_list = Tattoo.objects.all()
    args = {"tattoos" : tattoo_list}
    return render(request, 'homepage/homepage.html', args)
