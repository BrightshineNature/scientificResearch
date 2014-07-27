# coding: UTF-8
'''
Created on 2014-06-07

Desc: school' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.db.models import Q

from common.views import scheduleManage, researchConcludingManage,noticeMessageSettingBase
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from teacher.forms import SettingForm
from adminStaff.models import ProjectSingle, Re_Project_Expert
from users.models import ExpertProfile
from users.models import ExpertProfile, SchoolProfile
from common.utils import status_confirm,APPLICATION_SCHOOL_CONFIRM
from backend.logging import loginfo
from school.forms import FilterForm
from backend.utility import getContext
from const import *

def appView(request):
    context = {}
    return render(request,"school/application.html",context)
def scheduleView(request):

    userauth = {
                "role": "school",
                "status":"application"
    }
    return scheduleManage(request, userauth)



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
    expert_list = ExpertProfile.objects.all()
    unalloc_project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    alloc_project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    form = FilterForm(request = request)
    expert_form = FilterForm()
    
    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True)).count()
    
    context = {"form": form,
               "expert_form": expert_form,
               "page_info": "alloc",}
    context.update(getContext(unalloc_project_list, 1, "item", 0))
    context.update(getContext(alloc_project_list, 1, "item2", 0))
    context.update(getContext(expert_list, 1, "item3", 0))

    return render(request, "school/alloc.html", context)

def researchConcludingView(request):
    userauth={
        "role":"school",
        "status":"research_concluding",
    }
    return researchConcludingManage(request,userauth)

def finalAllocView(request):
    expert_list = ExpertProfile.objects.all()
    unalloc_project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_FINAL_SCHOOL_OVER)
    alloc_project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT)
    form = FilterForm(request = request)
    expert_form = FilterForm()
    
    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = False)).count()
    
    context = {"form": form,
               "expert_form": expert_form,
               "page_info": "finalalloc",}
    context.update(getContext(unalloc_project_list, 1, "item", 0))
    context.update(getContext(alloc_project_list, 1, "item2", 0))
    context.update(getContext(expert_list, 1, "item3", 0))

    return render(request, "school/alloc.html", context)

def noticeMessageSettingView(request):
    userauth={
        "role":"school"
    }
    return noticeMessageSettingBase(request,userauth)

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

