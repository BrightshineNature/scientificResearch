# coding: UTF-8
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string

from const import *
from users.models import Special,ExpertProfile,TeacherProfile,SchoolProfile,CollegeProfile
from adminStaff.forms import NewsForm, SpecialForm, CollegeForm,TemplateNoticeMessageForm
from django import  forms
from adminStaff.forms import TemplateNoticeMessageForm,DispatchForm,DispatchAddCollegeForm
from django.utils import simplejson
from django.template.loader import render_to_string
from dajaxice.utils import deserialize_form
from adminStaff.models import TemplateNoticeMessage
from backend.logging import loginfo
from common.sendEmail import sendemail

@dajaxice_register
def saveSpecialName(request, form):
    form = SpecialForm(deserialize_form(form))

    if form.is_valid():
        p = Special(name = form.cleaned_data['name'])
        p.save()
        return simplejson.dumps({'status':'1'})
    else :
        return simplejson.dumps({'status':'0'})

@dajaxice_register
def deleteSpecialName(request, checked):

    tag = False
    for i in checked:
        Special.objects.filter(id = i).delete()
        tag = True
    if tag :
        return simplejson.dumps({'status':'1'})
    else:
        return simplejson.dumps({'status':'0'})

@dajaxice_register
def allocSpecial(request, user, alloced):

    user = SchoolProfile.objects.filter(userid__username = user)

    all_spe = Special.objects.all()
    for spe in all_spe:
        if alloced.count(spe.name):
            spe.school_user = user[0]
        elif spe.school_user == user[0]:
            spe.school_user = None
        spe.save()
    return simplejson.dumps({'status':'1'})

@dajaxice_register
def TemplateNoticeChange(request,template_form,mod):
    if mod==-1:
        template_form=TemplateNoticeMessageForm(deserialize_form(template_form))
        template_form.save()
    else:
        template_notice=TemplateNoticeMessage.objects.get(pk=mod)
        f=TemplateNoticeMessageForm(deserialize_form(template_form),instance=template_notice)
        f.save()
    table=refresh_template_notice_table(request)
    ret={"status":'0',"message":u"模版消息添加成功","table":table}
    return simplejson.dumps(ret)
def refresh_template_notice_table(request):
    template_notice_message_form=TemplateNoticeMessageForm
    template_notice_message=TemplateNoticeMessage.objects.all()
    template_notice_message_group=[]
    cnt=1
    for item in template_notice_message:
        nv={
            "id":item.id,
            "iid":cnt,
            "title":item.title,
            "message":item.message,
        }
        cnt+=1
        template_notice_message_group.append(nv)
    return render_to_string("widgets/template_notice_table.html",{
            "template_notice_message_form":template_notice_message_form,
            "template_notice_message_group":template_notice_message_group,
    })
@dajaxice_register
def TemplateNoticeDelete(request,deleteID):
    template_notice=TemplateNoticeMessage.objects.get(pk=deleteID)
    template_notice.delete()
    table=refresh_template_notice_table(request)
    ret={"status":'0',"message":u"模版消息删除成功","table":table}
    return simplejson.dumps(ret)

@dajaxice_register
def Dispatch(request,form,identity):
    if identity == SCHOOL_USER or identity ==COLLEGE_USER:
        dispatchForm = DispatchForm(deserialize_form(form))
    elif identity == EXPERT_USER or identity == TEACHER_USER:
        dispatchForm = DispatchAddCollegeForm(deserialize_form(form))
    else:
        dispatchForm = DispatchForm(deserialize_form(form))
    if dispatchForm.is_valid():
        username = dispatchForm.cleaned_data["username"]
        password = dispatchForm.cleaned_data["password"]
        email = dispatchForm.cleaned_data["email"]
        person_name = dispatchForm.cleaned_data["person_firstname"]
        if password == "":
            password = username
        if identity == SCHOOL_USER or identity ==COLLEGE_USER:
            flag = sendemail(request, username, password,email,identity, person_name)
        elif identity == EXPERT_USER or identity == TEACHER_USER:
            college = dispatchForm.cleaned_data["college"]
            loginfo(college)
            flag = sendemail(request, username, password,email,identity, person_name,college=college)
        if flag:
            message = u"发送邮件成功"
            table = refresh_user_table(request,identity)
            return simplejson.dumps({'field':dispatchForm.data.keys(), 'status':'1', 'message':message,'table':table})
        else:
            message = u"用户名已存在"
            return simplejson.dumps({'field':dispatchForm.data.keys(), 'status':'1', 'message':message})
    else:
        return simplejson.dumps({'field':dispatchForm.data.keys(),'error_id':dispatchForm.errors.keys(),'message':u"输入有误"})
def refresh_user_table(request,identity):
    if identity == SCHOOL_USER:
        school_users = SchoolProfile.objects.all()
        return render_to_string("widgets/dispatch/school_user_table.html",
                            {"school_users":school_users})
    elif identity == COLLEGE_USER:
        college_users = CollegeProfile.objects.all()
        return render_to_string("widgets/dispatch/college_user_table.html",
                            {"college_users":college_users})
    elif identity == TEACHER_USER:
         users = TeacherProfile.objects.all()
    elif identity == EXPERT_USER:
        users = ExpertProfile.objects.all()
    return render_to_string("widgets/dispatch/user_addcollege_table.html",
                            {"users":users})
