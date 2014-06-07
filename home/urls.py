# coding: UTF-8
'''
Desc: urls of home

'''
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from home import views as home_views


urlpatterns = patterns('',
                       url(r'^$',
                           home_views.index,
                           name='homepage',
                           ),
                       )
