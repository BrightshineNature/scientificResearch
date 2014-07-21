# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin
from adminStaff.models import ProjectSingle,Special,College


RegisterClass = (
    ProjectSingle,
    Special,
    College,
)

for temp in RegisterClass:
    admin.site.register(temp)
