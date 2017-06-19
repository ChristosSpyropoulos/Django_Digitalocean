"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from helloworld import views as helloworld_v
from homepage import views as homepage_views
from about import views as about_views
from contact import views as contact_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', helloworld_v.hello),
    url(r'^home/', include('home.urls')),
    url(r'^watson/', include('watson.urls')),
    url(r'^homepage/$', homepage_views.home),
    url(r'^about/$', about_views.about),
    url(r'^contact/$', contact_views.contact),
]
