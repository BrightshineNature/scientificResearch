# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin
from common.models import *


RegisterClass = (
    BasisContent,
    BaseCondition,
    UploadFile,
)

for temp in RegisterClass:
    admin.site.register(temp)

class ProjectMemberAdmin(admin.ModelAdmin):
    search_fields = ['name','card']

RegisterSearchClass = (
    (ProjectMember,ProjectMemberAdmin),
)

for temp in RegisterSearchClass:
    admin.site.register(temp[0],temp[1])
