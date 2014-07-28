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
from backend.logging import loginfo
from django.conf import settings
from const import *
from adminStaff.models import ProjectSingle
from common.utils import status_confirm
from const.models import ScienceActivityType
from adminStaff.models import ProjectSingle
from common.forms import ProjectInfoForm, ProjectMemberForm
from common.models import ProjectMember

from adminStaff.models import ProjectSingle,Re_Project_Expert
from common.forms import ProjectInfoForm
from django.core.mail import send_mail
from users.models import AdminStaffProfile,TeacherProfile,ExpertProfile
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
def SendMail(request,form):
    form=deserialize_form(form)
    loginfo(form)
    
    #send_mail(form["mail_title"],form["mail_content"],"zhc1009@163.com",["347096491@qq.com","369385153@qq.com"])
    if form["mail_title"]=="":
        status=1
    elif form["mail_content"]=="":
        status=2
    else:
        recipient_list=[]
        if form.get("special"):
            special_group=SchoolProfile.objects.all()
            recipient_list.extend([item.userid.email for item in special_group])
        if form.get("college"):
            college_group=CollegeProfile.objects.all()
            recipient_list.extend([item.userid.email for item in college_group])
        if form.get("teacher"):
            if AdminStaffProfile.objects.filter(userid=request.user).count()>0:
                teacher_group=TeacherProfile.objects.all()
                recipient_list.extend([item.userid.email for item in teacher_group])
            else:
                year_group=form.getlist("teacher_year")
                sp_group=form.getlist("teacher_special")
                sp_group=[int(item) for item in sp_group]
                project_group=ProjectSingle.objects.filter(application_year__in=year_group,project_special__in=sp_group)
                teacher_group=[item.teacher for item in project_group]
                recipient_list.extend([item.userid.email for item in teacher_group])
        if form.get("expert"):
            if AdminStaffProfile.objects.filter(userid=request.user).count()>0:
                expert_group=ExpertProfile.objects.all()
                recipient_list.extend([item.userid.email for item in expert_group])
            else:
                year_group=form.getlist("expert_year")
                sp_group=form.getlist("expert_special")
                sp_group=[int(item) for item in sp_group]
                project_group=ProjectSingle.objects.filter(application_year__in=year_group,project_special__in=sp_group)
                expert_group=[]
                for project in project_group:
                    p_e_group=Re_Project_Expert.objects.filter(project=project)
                    expert_group.extend([item.expert for item in p_e_group])
                expert_group=list(set(expert_group))
                recipient_list.extend([item.userid.email for item in expert_group])
        if len(recipient_list)==0:
            status=3
        else:
            status=0
            send_mail(form["mail_title"],form["mail_content"],settings.DEFAULT_FROM_EMAIL,["347096491@qq.com","369385153@qq.com"])
    return simplejson.dumps({"status":status})

@dajaxice_register
def getStatus(request):
    return simplejson.dumps({
        "application_c":PROJECT_STATUS_APPLICATION_COMMIT_OVER,
        "application_s":PROJECT_STATUS_APPLICATION_COLLEGE_OVER,
        "final":PROJECT_STATUS_FINAL_COMMIT_OVER,
    })
@dajaxice_register
def LookThroughResult(request,judgeid,userrole,userstatus,look_through_form):
    project=ProjectSingle.objects.get(pk=judgeid)
    form=deserialize_form(look_through_form)
    if form["judgeresult"]=="1":
        status_confirm(project,-1)
    else:
    
        comment={
            "Judger":request.user.last_name,
            "Article":form.getlist('application').extend(form.getlist("final")),
            "description":form["reason"]
        }
        project.comment=eval(comment)
        project.save()
        statusRollBack(project,userrole,userstatus,form)
    context=schedule_form_data(request,{
        "role":userrole,
        "status":userstatus
    })
    if userstatus=="application":
        table_html=render_to_string("widgets/project_filter.html",context)
    else:
        table_html=render_to_string("widgets/research_concluding_table.html",context)
    return simplejson.dumps({"table_html":table_html})   
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



@dajaxice_register
def saveProjectInfoForm(request, form, pid):
    form = ProjectInfoForm(deserialize_form(form))


    p = ProjectSingle.objects.get(project_id = pid)
    if form.is_valid():        
        p.title = form.cleaned_data['project_name']
        science_type =form.cleaned_data['science_type']
        scienceType = ScienceActivityType.objects.get(category=science_type)
        p.science_type = scienceType
        p.trade_code = form.cleaned_data['trade_code']
        p.subject_name = form.cleaned_data['subject_name']
        p.subject_code = form.cleaned_data['subject_code']
        p.start_time = form.cleaned_data['start_time']
        p.end_time = form.cleaned_data['end_time']
        p.project_tpye = form.cleaned_data['project_tpye']
        p.save()            
        pass
    else :
        print "error in saveProjectInfoForm"


@dajaxice_register
def saveProjectMember(request, form, pid):
    form = ProjectMemberForm(deserialize_form(form))

    if form.is_valid():
        print form
        form.save()
    else:
        print form.errors
        print "error in saveProjectMember"




