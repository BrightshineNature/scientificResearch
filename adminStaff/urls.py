'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from adminStaff import views as adminStaff_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(
        r'^noticeMessageSetting$',
        adminStaff_views.noticeMessageSetting,
    ),
   url(r'^$', adminStaff_views.scheduleView,),

   url(r'^news_release$',adminStaff_views.newsRelease),
   url(
        r'^noticeMessageSetting$',
        adminStaff_views.noticeMessageSetting,
    ),
    url(
        r'^dispatch$',
        adminStaff_views.dispatchView,
    ),
    url(
        r'financialinfo$',
        adminStaff_views.financialInfoView,
    ),
 )
urlpatterns += staticfiles_urlpatterns()
