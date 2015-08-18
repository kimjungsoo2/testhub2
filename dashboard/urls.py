#!/usr/bin/env python

from django.conf.urls import patterns, url
from dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='nav_menu'),
)