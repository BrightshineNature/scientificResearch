# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin
from adminStaff.models import *


RegisterClass = (
    Re_Project_Expert,
    BasicScientificResearchScoreTable,
    HumanitiesSocialSciencesResearchScoreTable,
    MajorProjectScoreTable,
    KeyLaboratoryProjectScoreTable,
    FrontAndIntercrossResreachScoreTable,
    ScienceFoundationResearchScoreTable,
    OutstandingYoungResreachScoreTable,
    HomePagePic,
)

for temp in RegisterClass:
    admin.site.register(temp)

class ProjectSingleAdmin(admin.ModelAdmin):
    search_fields = ['project_code','title']

RegisterSearchClass = (
    (ProjectSingle,ProjectSingleAdmin),
)

for temp in RegisterSearchClass:
    admin.site.register(temp[0],temp[1])
