from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testhub2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^testbrowser/', include('testbrowser.urls', namespace='testbrowser')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
)
