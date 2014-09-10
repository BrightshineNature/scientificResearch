# coding: UTF-8
import os, sys,pickle
import time
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.db.models import Q
from backend.utility import getContext

from adminStaff.utility import getCollege
from django.utils import simplejson
from django.template.loader import render_to_string
from common.utility import get_xls_path
from const import *
from users.models import Special,ExpertProfile,TeacherProfile,SchoolProfile,CollegeProfile
from adminStaff.models import ProjectSingle,HomePagePic
from adminStaff.forms import TemplateNoticeMessageForm
from django import  forms
from adminStaff.forms import TemplateNoticeMessageForm,DispatchForm,DispatchAddCollegeForm
from django.utils import simplejson
from django.template.loader import render_to_string
from dajaxice.utils import deserialize_form
from adminStaff.models import TemplateNoticeMessage,ProjectSingle,News
from backend.logging import loginfo

from users.models import SchoolProfile,CollegeProfile,Special,College
from teacher.models import TeacherInfoSetting
from backend.logging import logger
from   adminStaff.forms      import ObjectForm

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
        'object_name':object,
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
            'object_name':object,    
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
            'object': object,
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

    context = {
        'status': 1 ,
        'objects_table': "",
    }
    if form.is_valid():
        if Object.objects.filter(name = form.cleaned_data['name']):
            print "hh" 
            context['status'] = 0
        else :
            print "OK"
            p = Object(name = form.cleaned_data['name'])
            p.save()
    else :
        context['status'] = 0
        pass

    context['objects_table'] = refreshObjectTable(request, object)

    return simplejson.dumps(context)

@dajaxice_register
def deleteObjectName(request, object, deleted):



    context = {
        'status':0 ,
        'objects_table': None,
        'object':object,
        'alloced':"",
    }


    if not deleted: 
        context['status']  = 0
    else:

        alloced = "["
        for i in deleted:
            if object == "special":
                cnt = Special.objects.get(name = i)
                if ProjectSingle.objects.filter(project_special = cnt):
                    if alloced != "[": alloced += ','
                    alloced += unicode(cnt.name)
            else:
                cnt = College.objects.get(name = i)
                if ProjectSingle.objects.filter(teacher__college = cnt):
                    if alloced != "[": alloced += ','
                    alloced += unicode(cnt.name)

        if alloced != "[":
            alloced += "]"
            context['status'] = 0
            context['alloced'] = alloced
            # print "***********()()"
            # print context['alloced']
        else :
            context['status'] = 1
            for i in deleted:
                if object == "special": 
                    cnt = Special.objects.filter(name = i)
                else:
                    cnt = College.objects.filter(name = i)
                cnt.delete()


    context['objects_table'] = refreshObjectTable(request, object)
    return simplejson.dumps(context)

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
@dajaxice_register
def Dispatch(request,form,identity,page):
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
            table = refresh_user_table(request,identity,page)
            return simplejson.dumps({'field':dispatchForm.data.keys(), 'status':'1', 'message':message,'table':table})
        else:
            message = u"用户名已存在"
            return simplejson.dumps({'field':dispatchForm.data.keys(), 'status':'1', 'message':message})
    else:
        return simplejson.dumps({'field':dispatchForm.data.keys(),'error_id':dispatchForm.errors.keys(),'message':u"输入有误"})
@dajaxice_register
def DispatchPagination(request,page,identity):
    html = refresh_user_table(request,identity,page)
    return simplejson.dumps({'html':html})

def refresh_user_table(request,identity,page=1):
    if identity == SCHOOL_USER:
        school_users = SchoolProfile.objects.all()
        context=getContext(school_users, page, "item")
        return render_to_string("widgets/dispatch/school_user_table.html",
                                context)
    elif identity == COLLEGE_USER:
        college_users = CollegeProfile.objects.all()
        context=getContext(college_users, page, "item2")
        return render_to_string("widgets/dispatch/college_user_table.html",
                                context)
    elif identity == TEACHER_USER:
         colleges = getCollege(request)
         qset = reduce(lambda x,y:x|y,[Q(college = _college) for _college in colleges])
         users = TeacherProfile.objects.filter(qset)
         context=getContext(users, page, "item")
         return render_to_string("widgets/dispatch/teacher_user_table.html",
                                context)
    elif identity == EXPERT_USER:
        users = ExpertProfile.objects.all()
        context=getContext(users, page, "item3")
        return render_to_string("widgets/dispatch/expert_user_table.html",
                                context)

@dajaxice_register
def infoExport(request,eid):
    proj_set = ProjectSingle.objects.all()
    path = get_xls_path(request,eid,proj_set,"优秀人才")
    ret = {'path':path}
    return simplejson.dumps(ret)

@dajaxice_register
def getTeacherInfo(request, name):
    message = ""
    setting_list = TeacherInfoSetting.objects.filter(name = name)
    context = {"setting_list": setting_list, }
    html = render_to_string("adminStaff/widgets/modify_setting_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def modifyTeacherInfo(request, name, card, id):
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
def change_project_unique_code(request, project_id,project_unique_code):
    '''
    change project_unique_code
    '''
    project_obj = ProjectSingle.objects.get(project_id = project_id)
    try:
        if ProjectSingle.objects.filter(project_code = project_unique_code).count():
            raise
        project_obj.project_code = project_unique_code
        project_obj.save()
        # if len(project_unique_code.strip()) == 0:
        #     project_unique_code = "无"
    except Exception, e:
        loginfo(e)
        project_unique_code = "error"
    return simplejson.dumps({'status':'1', 'res':project_unique_code})
@dajaxice_register
def getNewsReleasePagination(request,page):
    message=""
    page =int(page)
    newsList = News.objects.all()
    context = getContext(newsList,page,"item",page_elems=7)
    html = render_to_string("adminStaff/widgets/newslist.html",context)
    return simplejson.dumps({"message":message,"html":html})
@dajaxice_register
def FileDeleteConsistence(request, fid):
    """
    Delete files in history file list
    """
    logger.info("sep delete files"+"**"*10)
    # check mapping relation
    f = get_object_or_404(HomePagePic, id=fid)

    if request.method == "POST":
        try:
            os.remove(f.pic_obj.url)
            f.delete()
        except: pass
        return simplejson.dumps({"is_deleted": True,
                                 "message": "delete it successfully!",
                                 "fid": str(fid)})
    else:
        return simplejson.dumps({"is_deleted": False,
                                 "message": "Warning! Only POST accepted!"})
