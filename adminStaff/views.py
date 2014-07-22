# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from adminStaff.forms import NewsForm, SpecialForm, CollegeForm,TemplateNoticeMessageForm,DispatchForm,DispatchAddCollegeForm
from adminStaff.models import TemplateNoticeMessage, Special
from users.models import SchoolProfile,CollegeProfile,ExpertProfile
from const import NOTICE_CHOICE
from backend.logging import loginfo

def appView(request):

    context = {}
    return render(request, "adminStaff/application.html", context)

def allocManageView(request):


    userauth = {
        'role': 'adminStaff',
    }

    special_form = SpecialForm()
    college_form = CollegeForm()

    if request.method == "POST":
        special_form = SpecialForm(request.POST)

    school_user = SchoolProfile.objects.all()
    special_list = Special.objects.all()    


    special_user_info = {}
    for i in school_user:
        special_user_info[i] = []  

    for i in special_list:
        print i.school_user

        if i.school_user:
            special_user_info[i.school_user].append(i.name)
    



    


    college_list = {
        "计算机",
        "物理",
    }

    # print "$$"
    # print special_list[0].name
    # print special_list[0].school_user
    

    context = { 'special_form' : special_form,
                'special_list': special_list,
                'special_user_info': special_user_info, 
                'college_form': college_form, 
                'college_list': college_list,
    }

    return render(request, "adminStaff/alloc_manage.html", context)
def scheduleView(request):


    userauth = {
        'role': 'adminStaff',
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
