# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

from adminStaff.forms import NewsForm, SpecialForm, CollegeForm

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


    return scheduleManage(request, userauth)

def newsRelease(request):
    context={}
    context.update({"newsform":NewsForm})
    return render(request,"adminStaff/news_release.html",context)
def noticeMessageSetting(request):
    context={}
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
