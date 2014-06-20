'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from school import views as school_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',

    url( r'^$', school_views.scheduleView,  ),
	url(
		r'final$',
		school_views.final_report_view,
	),
    url(
        r'progress',
        school_views.progressReportView,
    ),
    url(
        r'alloc',
        school_views.allocView,
    ),
)
urlpatterns += staticfiles_urlpatterns()
