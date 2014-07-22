# coding: UTF-8
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string

from users.models import Special
from adminStaff.forms import NewsForm, SpecialForm, CollegeForm,TemplateNoticeMessageForm
from django import  forms
from adminStaff.forms import TemplateNoticeMessageForm
from django.utils import simplejson
from django.template.loader import render_to_string
from dajaxice.utils import deserialize_form
from adminStaff.models import TemplateNoticeMessage
from backend.logging import loginfo

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
    school_form = SchoolDictDispatchForm(deserialize_form(form))
    if school_form.is_valid():
        password = school_form.cleaned_data["school_password"]
        email = school_form.cleaned_data["school_email"]
        name = email
        school_name = school_form.cleaned_data["school_name"]
        person_name = school_form.cleaned_data["school_personname"]
        if password == "":
            password = email.split('@')[0]
        flag = AdminStaffService.sendemail(request, name, password,email,SCHOOL_USER, school_name=school_name,person_name = person_name)
        loginfo(flag)
        if flag:
            message = u"发送邮件成功"
            table = refresh_mail_table(request)
            return simplejson.dumps({'field':school_form.data.keys(), 'status':'1', 'message':message, 'table': table})
        else:
            message = u"相同邮件已经发送，中断发送"
            return simplejson.dumps({'field':school_form.data.keys(), 'status':'1', 'message':message})
    else:
        return simplejson.dumps({'field':school_form.data.keys(),'error_id':school_form.errors.keys(),'message':u"输入有误"})
