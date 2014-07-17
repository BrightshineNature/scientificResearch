# coding: UTF-8
'''
Created on 2014-06-07

Desc: school' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from adminStaff.models import ProjectSingle
from backend.logging import loginfo

def appView(request):
    context = {}
    return render(request,"school/application.html",context)
def scheduleView(request):
    not_pass_apply_project_group=ProjectSingle.objects.filter(project_status=0)
    pass_apply_project_group=ProjectSingle.objects.filter(project_status__gt=0)
    param={
        "not_pass_apply_project_group":not_pass_apply_project_group,
        "pass_apply_project_group":pass_apply_project_group,
    }
    userauth = {
                "role": 'school',                
    }
    return scheduleManage(request, userauth,param)


def financialView(request):
    userauth = {
                "role": 'school',                
    }
    return financialManage(request, userauth)


def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"school/project_financial_info.html",context)

def finalReportView(request):
    context = {}
    return render(request,"school/final.html",context)
def progressReportView(requset):
    context={}
    return render(requset,"school/progress.html",context)

def allocView(request):
    context = {}
    return render(request, "school/alloc.html", context)
def researchConcludingView(request):
    context={
        "school":True
    }
    return render(request,"school/research_concluding.html",context)

def finalAllocView(request):
    context = {}
    return render(request, "school/final_alloc.html", context)
def noticeMessageSettingView(request):
    context = {}
    return render(request, "school/notice.html", context)

def controlView(request):
    

    special = [     
              {
                'year_list': [2015,],
                'special_name': 'science',
    },
              {
                'year_list': [2011,2012,2013,2014,],
                'special_name': 'liberal',
    },
        
    ]


    
    context = {
        'special' :special,
    }
    return render(request, "school/control.html", context);
