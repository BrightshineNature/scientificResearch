# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

from adminStaff.forms import NewsForm, SpecialForm

def specialView(request):


    userauth = {
        'role': 'adminStaff',
    }
    special_form = SpecialForm()

    if request.method == "POST":
        special_form = SpecialForm(request.POST)


    special_dict = {
        "文科",
        "理科",

    }

    context = {'special_form' : special_form,
                'special_dict': special_dict,
    }
    

    return render(request, "adminStaff/special.html", context)


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
