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
from adminStaff.forms import TemplateNoticeMessageForm
from django import  forms
from adminStaff.forms import TemplateNoticeMessageForm,DispatchForm,DispatchAddCollegeForm
from django.utils import simplejson
from django.template.loader import render_to_string
from dajaxice.utils import deserialize_form
from adminStaff.models import TemplateNoticeMessage,News
from backend.logging import loginfo
from users.models import SchoolProfile,CollegeProfile,Special,College
from teacher.models import TeacherInfoSetting
from backend.logging import logger

def getObject(object):
    if object == "special":
        return Special
    elif object == "college":
        return College
    else :
        print "error in getObject"
        return None
def refreshObjectTable(request, object):

    object_list = []
    if(object == "special"):
        for i in Special.objects.all() :
            object_list.append({'name':i.name, 'user':i.school_user, })
    elif object == "college":
        for i in College.objects.all() :
            object_list.append({'name':i.name, 'user':i.college_user, })

    instance = {
        'object_list': object_list
    }
    return render_to_string("adminStaff/widgets/objects_table.html", {'instance': instance})
def refreshObjectAlloc(request, object):

    if object == "special":

        user_special_info = {}

        for i in SchoolProfile.objects.all():
            user_special_info[i] = []   
        
        for i in Special.objects.all():
            if i.school_user:
                user_special_info[i.school_user].append(i.name)
        instance = {
            'object_chinese_name':'专题',
            'user_object_info':user_special_info,
        }
        return render_to_string("adminStaff/widgets/object_alloc.html", {'instance': instance})
    elif object == "college":
        user_college_info = {}

        for i in CollegeProfile.objects.all():
            user_college_info[i] = []   
        
        for i in College.objects.all():
            if i.college_user:
                user_college_info[i.college_user].append(i.name)
        instance = {
            'object_chinese_name':'学院',
            'user_object_info':user_college_info,
        }
        return render_to_string("adminStaff/widgets/object_alloc.html", {'instance': instance})

    else:
        loginfo("error in refreshObjectAlloc")

















from common.sendEmail import sendemail

@dajaxice_register
def saveObjectName(request, object, form):

    print "save*****"
    print object
    form = ObjectForm(deserialize_form(form))

    Object = getObject(object)


    if form.is_valid():        
        p = Object(name = form.cleaned_data['name'])
        print ""
        print p.name
        p.save()
    else :
        pass

    return simplejson.dumps({'status':'1' , 
        'objects_table': refreshObjectTable(request, object)
        })

@dajaxice_register
def deleteObjectName(request, object, deleted):

    
    Object = getObject(object)

    for i in deleted:
        cnt = Object.objects.filter(name = i)        
        Object.objects.filter(name = i).delete()
    return simplejson.dumps({'status':'1' , 
        'objects_table': refreshObjectTable(request, object)
        })

@dajaxice_register
def allocObject(request, object, user, alloced):
    
    filter_user = user
    if object == "special":
        user = SchoolProfile.objects.filter(userid__username = filter_user)[0]
    elif object == "college":

        user = CollegeProfile.objects.filter(userid__username = filter_user)[0]
    else:
        loginfo("error in allocObject")

    Object = getObject(object)
    objs = Object.objects.all()
    for o in objs:
        if object == "special":
            if alloced.count(o.name):
                o.school_user = user
            elif o.school_user == user:
                o.school_user = None
            o.save()
        elif object == "college":
            if alloced.count(o.name):
                o.college_user = user
            elif o.college_user == user:
                o.college_user = None
            o.save()
        else:
            loginfo("error in allocObject")


    return simplejson.dumps({'status':'1' , 
        'object_alloc': refreshObjectAlloc(request, object),
        'object_table': refreshObjectTable(request, object),
        })


@dajaxice_register
def getNoticePagination(request,page):
    message=""
    table=refresh_template_notice_table(request,page)
    ret={"message":message,"table":table}
    return simplejson.dumps(ret)
    

    Object = getObject(object)

    for i in deleted:
        cnt = Object.objects.filter(name = i)
        Object.objects.filter(name = i).delete()
    return simplejson.dumps({'status':'1' ,
        'objects_table': refreshObjectTable(request, object)
        })

@dajaxice_register
def allocObject(request, object, user, alloced):

    filter_user = user
    if object == "special":
        user = SchoolProfile.objects.filter(userid__username = filter_user)[0]
    elif object == "college":

        user = CollegeProfile.objects.filter(userid__username = filter_user)[0]
    else:
        loginfo("error in allocObject")

    Object = getObject(object)
    objs = Object.objects.all()
    for o in objs:
        if object == "special":
            if alloced.count(o.name):
                o.school_user = user
            elif o.school_user == user:
                o.school_user = None
            o.save()
        elif object == "college":
            if alloced.count(o.name):
                o.college_user = user
            elif o.college_user == user:
                o.college_user = None
            o.save()
        else:
            loginfo("error in allocObject")


    return simplejson.dumps({'status':'1' , 
        'object_alloc': refreshObjectAlloc(request, object),
        'object_table': refreshObjectTable(request, object),
        })

@dajaxice_register
def TemplateNoticeChange(request,template_form,mod,page):
    if mod==-1:
        template_form=TemplateNoticeMessageForm(deserialize_form(template_form))
        template_form.save()
    else:
        template_notice=TemplateNoticeMessage.objects.get(pk=mod)
        f=TemplateNoticeMessageForm(deserialize_form(template_form),instance=template_notice)
        f.save()
    table=refresh_template_notice_table(request,page)
    ret={"status":'0',"message":u"模版消息添加成功","table":table}
    return simplejson.dumps(ret)
def refresh_template_notice_table(request,page):
    template_notice_message_form=TemplateNoticeMessageForm
    template_notice_message=TemplateNoticeMessage.objects.all()
    template_notice_message_group=[]
    cnt=1
    page=int(page)
    for item in template_notice_message:
        nv={
            "id":item.id,
            "iid":cnt,
            "title":item.title,
            "message":item.message,
        }
        cnt+=1
        template_notice_message_group.append(nv)
    context=getContext(template_notice_message_group,page,"item",0)
    context.update({"template_notice_message_form":template_notice_message_form})
    return render_to_string("widgets/template_notice_table.html",context)
@dajaxice_register
def TemplateNoticeDelete(request,deleteID,page):
    template_notice=TemplateNoticeMessage.objects.get(pk=deleteID)
    template_notice.delete()
    table=refresh_template_notice_table(request,page)
    #.c.c.oginfo(table)
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

@dajaxice_register
def getTeacherInfo(request, name):
    message = ""
    setting_list = TeacherInfoSetting.objects.filter(name = name)
    context = {"setting_list": setting_list, }
    html = render_to_string("adminStaff/widgets/modify_setting_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def modifyTeacherInfo(request, name, card, id):
    print "here"*100
    message = ""
    try:
        if len(name) == 0 or len(card) == 0: raise

        setting = TeacherInfoSetting.objects.get(id = id)
        setting.name = name
        setting.card = card
        setting.save()
        message = "ok"
    except:
        message = "fail"

    return simplejson.dumps({"message": message, })
@dajaxice_register
def get_news_list(request, uid):

    logger.info("sep delete news"+"**"*10)
    # check mapping relation
    try:
        delnews=News.objects.get(id=uid)
        logger.info(delnews.id)
        if request.method == "POST":
            delnews.delete()
            return simplejson.dumps({"is_deleted": True,
                    "message": "delete it successfully!",
                    "uid": str(uid)})
        else:
            return simplejson.dumps({"is_deleted": False,
                                     "message": "Warning! Only POST accepted!"})
    except Exception, err:
        logger.info(err)
