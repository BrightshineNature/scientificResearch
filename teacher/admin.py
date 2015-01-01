# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin 

from teacher.models import *

RegisterClass = (
	FinalSubmit,
	ProjectAchivement,
    ProjectStatistics,
    TeacherInfoSetting,
	ProjectFundSummary,
	ProjectFundBudget,
    ProgressReport,
)

for temp in RegisterClass:
    admin.site.register(temp)
