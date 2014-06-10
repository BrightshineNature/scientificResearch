'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from expert import views as expert_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(
        r'^$',
        expert_views.homeView,
    ),
)
urlpatterns += staticfiles_urlpatterns()
