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
        r'dispatch$',
        college_views.dispatchView,
    ),
	url(
        r'^final/(?P<pid>.{36})$',
		college_views.finalReportView,
	),
    url(
        r'^application/(?P<pid>.{36})$',
        college_views.appView,
    ),

    url(
        r'financial$',
        college_views.financialView,
    ),
    url(
        r'financialinfo$',
        college_views.financialInfoView,
    ),
    url( 
        r'researchconcluding$',
        college_views.researchConcludingView,
    ),
    url(
        r'dispatch$',
        college_views.dispatchView,
    ),
    url(
        r'^finalinfo/(?P<pid>.{36})$',
        college_views.finalInfoView,
    ),
    url(
        r'^fundbudget/(?P<pid>.{36})$',
        college_views.fundBudgetView,
    ),
    url(
        r'file_upload/(?P<pid>.{36})$',
        college_views.fileUploadManageView,
    ),
)
urlpatterns += staticfiles_urlpatterns()
