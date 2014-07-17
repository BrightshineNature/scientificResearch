# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

from adminStaff.forms import NewsForm, SpecialForm, CollegeForm,TemplateNoticeMessageForm
from adminStaff.models import TemplateNoticeMessage
from const import NOTICE_CHOICE
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


    special_dict = {
        "文科",
        "理科",

    }
    college_dict = {
        "计算机",
        "物理",
    }

    context = {'special_form' : special_form,
                'special_dict': special_dict,
                'college_form': college_form, 
                'college_dict': college_dict,
    }
    

    return render(request, "adminStaff/alloc_manage.html", context)


from adminStaff.forms import NewsForm, SchoolDispatchForm, CollegeDispatchForm, ExpertDispatchForm
def scheduleView(request):


    userauth = {
        'role': 'adminStaff',
    }

    
    return scheduleManage(request, userauth,{})

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
    school_form = SchoolDispatchForm()
    college_form = CollegeDispatchForm()
    expert_form = ExpertDispatchForm()
    context = {"school_form": school_form, 
               "college_form": college_form, 
               "expert_form": expert_form, 
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
