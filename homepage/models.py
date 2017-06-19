# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

# Create your models here.


class Tattoo(models.Model):
        tattoo_type = models.CharField(max_length=255, default= '')
        tattoo_color = models.CharField(max_length=100, default= '')
        tattoo_place = models.CharField(max_length=100, default= '')
        tattoo_photo = models.ImageField(upload_to='tattoo_image')

admin.site.register(Tattoo)
