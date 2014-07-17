# coding: UTF-8
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string

from adminStaff.forms import NewsForm, SpecialForm, CollegeForm,TemplateNoticeMessageForm
from django import  forms
from adminStaff.models import Special

@dajaxice_register
def saveSpecialName(request, form):
    form = SpecialForm(deserialize_form(form))
    
    if form.is_valid():
        print form.cleaned_data['name']
        p = Special(name= form.cleaned_data['name'])
        p.save()


    return simplejson.dumps({'status':'1', 'res':"res"})
from adminStaff.forms import TemplateNoticeMessageForm
from django.utils import simplejson
from django.template.loader import render_to_string
from dajaxice.utils import deserialize_form
from adminStaff.models import TemplateNoticeMessage
from backend.logging import loginfo


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

