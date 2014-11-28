# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin
from adminStaff.models import *

# class ProjectSingle(admin.ModelAdmin):
#     search_fields = ['project_code','title']

RegisterClass = (
    ProjectSingle,
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
