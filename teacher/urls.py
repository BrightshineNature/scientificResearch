'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from teacher import views as teacher_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(
        r'^$',
        teacher_views.homeView,
    ),
	url(
		r'final$',
		teacher_views.final_report_view,
	),
)
urlpatterns += staticfiles_urlpatterns()
