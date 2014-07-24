# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from adminStaff.forms import NewsForm, ObjectForm, TemplateNoticeMessageForm,DispatchForm,DispatchAddCollegeForm
from adminStaff.models import TemplateNoticeMessage
from users.models import SchoolProfile,CollegeProfile,ExpertProfile,Special,College
from const import NOTICE_CHOICE
from backend.logging import loginfo

def appView(request):

    context = {}
    return render(request, "adminStaff/application.html", context)


def allocManageView(request):
    userauth = {
        'role': 'adminStaff',
    }



    object_form = ObjectForm()

    #special
    special_list = []
    user_special_info = {}
    for i in Special.objects.all() :
        special_list.append({'name':i.name, 'user':i.school_user, })

    for i in SchoolProfile.objects.all():
        user_special_info[i] = []   
    
    for i in special_list:
        if i['user']:
            user_special_info[i['user']].append(i['name'])

    # college
    college_list = []
    user_college_info = {}
    for i in College.objects.all() :
        college_list.append({'name':i.name, 'user':i.college_user, })

    for i in CollegeProfile.objects.all():
        user_college_info[i] = []   
    
    for i in college_list:
        if i['user']:
            user_college_info[i['user']].append(i['name'])
    



    


    instance_list = [ 
        {
            'object_chinese_name':"专题",
            'object_name': "special",
            'object_form': object_form,
            'object_list': special_list,
            'user_object_info':user_special_info,
        },
        {
            'object_chinese_name':"学院",
            'object_name': "college",
            'object_form': object_form,
            'object_list': college_list,
            'user_object_info':user_college_info,
        },
    ]

    

    context = { 
    'instance_list': instance_list,
    }

    return render(request, "adminStaff/alloc_manage.html", context)
def scheduleView(request):


    userauth = {
        'role': 'adminStaff',
        'status':'application'
    }
    return scheduleManage(request, userauth)

def newsRelease(request):
    context={}
    context.update({"newsform":NewsForm})
    return render(request,"adminStaff/news_release.html",context)
def noticeMessageSetting(request):
    notice_choice=NOTICE_CHOICE
    template_notice_message=TemplateNoticeMessage.objects.all()
    template_notice_message_form = TemplateNoticeMessageForm()
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

    context={
        "template_notice_message_form":template_notice_message_form,
        "notice_choice":notice_choice,
        "template_notice_message_group":template_notice_message_group,
    }
    return render(request,"adminStaff/notice_message_setting.html",context)

def dispatchView(request):
    dispatch_form = DispatchForm()
    dispatchAddCollege_form=DispatchAddCollegeForm()
    college_users = CollegeProfile.objects.all()
    expert_users = ExpertProfile.objects.all()
    school_users = SchoolProfile.objects.all()
    loginfo(college_users.count())
    loginfo(school_users.count())
    context = {
               "dispatch_form":dispatch_form,
               "dispatchAddCollege_form":dispatchAddCollege_form,
               "college_users":college_users,
               "school_users":school_users,
               "users":expert_users,
    }
    return render(request, "adminStaff/dispatch.html", context)
def financialView(request):
    userauth = {
                "role": 'adminStaff', 
    }
    return financialManage(request, userauth)


def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"adminStaff/project_financial_info.html",context)
