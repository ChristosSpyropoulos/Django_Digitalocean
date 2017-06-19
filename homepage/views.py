# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from homepage.models import Tattoo

# Create your views here.
def home(request):
    import os
    # for file in os.listdir("C:/Users/Christos/Desktop/digitalocean/Django_Digitalocean/static/images"):
    #     if file.endswith(".jpg"):
    #         b = Tattoo(tattoo_type='oldschool',tattoo_color='black',tattoo_place='body',tattoo_photo=os.path.join("", file))
    #         b.save()
    tattoo_list = Tattoo.objects.all()
    args = {"tattoos" : tattoo_list}
    return render(request, 'homepage/homepage.html', args)
