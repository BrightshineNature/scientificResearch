# coding: UTF-8
'''
Created on 2014-06-07

Desc: school' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from backend.logging import loginfo
from backend.utility import getContext
from const import *
from common.utils import status_confirm,APPLICATION_SCHOOL_CONFIRM
from adminStaff.utility import getSpecial

from common.views import scheduleManage, researchConcludingManage,noticeMessageSettingBase, get_project_list

from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm,SettingForm
from adminStaff.models import ProjectSingle, Re_Project_Expert
from school.forms import FilterForm,ExpertReviewForm

from users.models import ExpertProfile, SchoolProfile

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def appView(request):
    context = {}
    return render(request,"school/application.html",context)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def scheduleView(request):

    userauth = {
                "role": "school",
                "status":"application"
    }
    return scheduleManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"school/project_financial_info.html",context)


@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def finalReportView(request):
    context = {}
    return render(request,"school/final.html",context)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def progressReportView(requset):
    context={}
    return render(requset,"school/progress.html",context)
    
@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def allocView(request):
    expert_list = ExpertProfile.objects.all()
    unalloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    alloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
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

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def researchConcludingView(request):
    userauth={
        "role":"school",
        "status":"research_concluding",
    }
    return researchConcludingManage(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def finalAllocView(request):
    expert_list = ExpertProfile.objects.all()
    unalloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_SCHOOL_OVER)
    alloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT)
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

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def noticeMessageSettingView(request):
    userauth={
        "role":"school"
    }
    return noticeMessageSettingBase(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def controlView(request):
    expert_review_forms=[]
    specials =  getSpecial(request)
    loginfo(specials)
    for special in specials:
        expert_review_form = ExpertReviewForm(instance=special)
        expert_review_forms.append(expert_review_form)
        control_types = []
        for t in CONTROL_TYPE_CHOICES:
            t = list(t)
            t.append(getattr(special,t[0]+"_status"))
            control_types.append(t)
        special.control_types = control_types
    spec_list = zip(specials,expert_review_forms)
    context = {
        'spec_list' :spec_list,
    }
    return render(request, "school/control.html", context);

