'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from finance import views as finance_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(
        r'^$',
        finance_views.applicationProjectView,
    ),
    url(
        r'concludingProject$',
        finance_views.concludingProjectView,
    ),
    url(
        r'financeBudget$',
        finance_views.financeBudgetView,
    ),
    url(
        r'financeAuditing$',
        finance_views.financeAuditingView,
    ),
    url(
        r'financial$',
        finance_views.financialView,
    ),
    url(
        r'financialinfo$',
        finance_views.financialInfoView,
    ),
    url(
        r'exportFinance$',
        finance_views.exportFinanceView,
    ),
)
urlpatterns += staticfiles_urlpatterns()
