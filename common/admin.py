# coding: UTF-8
'''
Created on 2013-3-27

@author: tianwei
'''

from django.contrib import admin
from common.models import *


RegisterClass = (
    
    ProjectMember,
    BasisContent,
    BaseCondition,
    UploadFile,
)

for temp in RegisterClass:
    admin.site.register(temp)