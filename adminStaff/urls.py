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
   url(r'^application$', adminStaff_views.appView,),

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
        r'alloc_manage$',
        adminStaff_views.allocManageView,
    ),
    url(
        r'financialinfo$',
        adminStaff_views.financialInfoView,
    ),
    url(
        r'financial$',
        adminStaff_views.financialView,
    ),
    url(
        r'infoModify$',
        adminStaff_views.infoModifyView,
    ),
    url(
        r'infoExport$',
        adminStaff_views.infoExportView,
    ),
    url(
        r'^finalinfo/(?P<pid>.{36})$',
        adminStaff_views.finalInfoView,
    ),
     url(
        r'^final/(?P<pid>.{36})$',
        adminStaff_views.finalReportView,
    ),
    url(
        r'^fundbudget/(?P<pid>.{36})$',
        adminStaff_views.fundBudgetView,
    ), 
    url(
        r'file_upload/(?P<pid>.{36})$',
        adminStaff_views.fileUploadManageView,
    ),
    url(
        r'homepic_import$',
        adminStaff_views.homepic_import_view,
    ),
    url(
        r'delete_project$',
        adminStaff_views.deleteProject,
    ),
    url(
        r'createProject$',
        adminStaff_views.createProject,
    ),
)
urlpatterns += staticfiles_urlpatterns()
