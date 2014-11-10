# coding: UTF-8
'''
Created on 2014-07-23

@author:
'''
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import active,login_redirect,logout_redirect
urlpatterns = patterns('',
          url(r'^active/(?P<activation_key>\w+)/$',active,name='registration_avtive'),
          url(r'^logout/$',auth_views.logout,{'next_page':'/accounts/logoutredirect'},name='auth_logout'),
          url(r'^password/change/$',auth_views.password_change,name='auth_password_change'),
          url(r'^password/change/done/$',auth_views.password_change_done, name='auth_password_change_done'),
          url(r'^password/reset/$',auth_views.password_reset, name='auth_password_reset'),
          url(r'^password/reset/confirm/(?P<uidb36>[0-9a-zA-Z]+)-(?P<token>.+)/$',auth_views.password_reset_confirm,name='auth_password_reset_confirm'),
          url(r'^password/reset/complete/$',auth_views.password_reset_complete,name='auth_password_reset_complete'),
          url(r'^password/reset/done/$',auth_views.password_reset_done,name='auth_password_reset_done'),
          url(r'^redirect/$', login_redirect, name="auth_login_redirect"),
          url(r'^adminlogin/$',auth_views.login,{'template_name':'registration/login_admin.html'},name='auth_adminlogin'),
          url(r'^collegelogin/$',auth_views.login,{'template_name':'registration/login_college.html'},name='auth_collegelogin'),
          url(r'^expertlogin/$',auth_views.login,{'template_name':'registration/login_expert.html'},name='auth_expertlogin'),
          url(r'^teacherlogin/$',auth_views.login,{'template_name':'registration/login_teacher.html'},name='auth_teacherlogin'),
          url(r'^loginredirect/(?P<identity>\w+)/$', login_redirect, name="auth_login_redirect"),
          url(r'^logoutredirect/$', logout_redirect, name="auth_logout_redirect"),

        )
