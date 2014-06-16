'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from college import views as college_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(r'^$', college_views.scheduleView, ),
	url(
		r'final$',
		college_views.final_report_view,
	),
)
urlpatterns += staticfiles_urlpatterns()
