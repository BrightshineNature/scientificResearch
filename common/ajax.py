# coding: UTF-8
'''
Created on 2013-3-29

@author: sytmac
'''
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string

#from adminStaff.forms import NumLimitForm, TimeSettingForm, SubjectCategoryForm, ExpertDispatchForm,SchoolDispatchForm,TemplateNoticeForm,FundsChangeForm,StudentNameForm, SchoolDictDispatchForm

from django.db.models import Q

from const import *


OVER_STATUS_NOTOVER = "notover"
OVER_STATUS_OPENCHECK = "opencheck"
OVER_STATUS_MIDCHECK = "midcheck"
OVER_STATUS_FINCHECK = "fincheck"
OVER_STATUS_NORMAL = "normal"

OVER_STATUS_CHOICES = (
    ('no', u"未结题"),
    ('yes', u"已结题"),    
)
@dajaxice_register
def change_project_overstatus(request, project_id, changed_overstatus):
    '''
    change project overstatus
    '''
    choices = dict(OVER_STATUS_CHOICES)



    res = choices[changed_overstatus]    
    return simplejson.dumps({'status':'1', 'res':res})

    if changed_overstatus in choices:
        AdminStaffService.ProjectOverStatusChange(project_id, changed_overstatus)
        res = choices[changed_overstatus]
    else:
        res = "操作失败，请重试"
    return simplejson.dumps({'status':'1', 'res':res})
