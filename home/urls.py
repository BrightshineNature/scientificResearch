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
                       url(r'show$',
                           home_views.show,
                          ),
                       url(r'show/(?P<project_id>.{36})$',
                           home_views.showProject,
                          ),
                       url(r'news/news_cate=(?P<news_cate>\S+)$',
                           home_views.newsListByCate,
                           ),
                       url(r'^news/(?P<news_id>\d+)$',
                           home_views.read_news,
                           name='read_news'
                           ),

                     )
