# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin
from adminStaff.models import ProjectSingle, Re_Project_Expert, BasicScientificResearchScoreTable


RegisterClass = (
    ProjectSingle,
    Re_Project_Expert,
    BasicScientificResearchScoreTable,
)

for temp in RegisterClass:
    admin.site.register(temp)
