# coding=utf-8
'''
 File Name: admin.py
 Author: shenlian
 Created Time: 2014年07月11日 星期五 10时13分50秒
'''
from django.contrib import admin
from const.models import *

RegisterClass = (
    AchivementTypeDict,
    StaticsTypeDict,
    StaticsDataTypeDict,
    UserIdentity,
    ProjectStatus,
    NewsCategory,
    ScienceActivityType,
    ExpertReview,
    ExecutivePosition,
    ProfessionalTitle,
    NationalTradeCode,
    Subject,
    ExpertFinalReview,
)

for temp in RegisterClass:
    admin.site.register(temp)
