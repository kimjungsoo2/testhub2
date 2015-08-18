#!/usr/bin/env python

from django.conf.urls import patterns, url
from testbrowser import views

urlpatterns = patterns('',
    url(r'^$', views.list_domains, name='nav_menu'),
    url(r'^list_secondary/$', views.list_secondary_domains, name='sec_domain_list'),
    url(r'^list_testplans/$', views.list_testplans, name='list_testplans'),
    url(r'^list_testcases/$', views.list_testcases, name='list_testcases'),
    #url(r'^testreport/$', views.generate_report, name='testreport'),
    url(r'^testreport/(?P<key>.*)$', views.generate_report, name='testreport'),   
)