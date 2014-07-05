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
		school_views.finalReportView,
	),
    url(
        r'application$',
        school_views.appView,
    ),
    url(
        r'progress',
        school_views.progressReportView,
    ),
    url(
        r'^alloc',
        school_views.allocView,
    ),
    url(
        r'^finalalloc',
        school_views.finalAllocView,
    ),
    url(
        r'control',
        school_views.controlView,
    ),
    url(
        r'financial$',
        school_views.financialView,
    ),
    url(
        r'financialinfo$',
        school_views.financialInfoView,
    ),
    url(
        r'researchconcluding$',
        school_views.researchConcludingView,
    )
)
urlpatterns += staticfiles_urlpatterns()
