# coding: UTF-8
'''
Created on 2014-06-07

Desc: college' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from backend.logging import loginfo
from const import *

from adminStaff.utility import getCollege
from common.views import scheduleManage, financialManage,researchConcludingManage

from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from adminStaff.forms import DispatchAddCollegeForm
from college.forms import TeacherDispatchForm

from users.models import TeacherProfile

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def appView(request):
    context = {}
    return render(request, "college/application.html", context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def scheduleView(request):
    userauth = {
            "role": 'college',
            "status":"application"  
                }

    return scheduleManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def financialView(request):
    userauth = {
                "role": 'college',                
    }
    return financialManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"college/project_financial_info.html",context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def finalReportView(request):
    context = {}
    return render(request,"college/final.html",context)
def researchConcludingView(request):
    userauth={
        'role':'college',
        'status':'research_concluding',
    }
    return researchConcludingManage(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def dispatchView(request):
    dispatchAddCollege_form=DispatchAddCollegeForm(user=request.user)
    teacher_users = TeacherProfile.objects.all()
    context = {
               "dispatchAddCollege_form":dispatchAddCollege_form,
               "users":teacher_users,
    }
    return render(request, "college/dispatch.html", context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def financialView(request):
    userauth = {
                "role": 'adminStaff', 
    }
    return financialManage(request, userauth)
    teacher_form = TeacherDispatchForm()
    context = {
        "teacher_form": teacher_form,
    }
    return render(request, "college/dispatch.html", context)
