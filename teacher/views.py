# coding: UTF-8
'''
Created on 2014-06-07

Desc: teacher' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from backend.logging import loginfo
from const import *

from common.views import scheduleManage,finalReportViewWork,appManage,fundBudgetViewWork 

from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm, SettingForm
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm

from users.models import TeacherProfile
from teacher.models import TeacherInfoSetting
from adminStaff.models import ProjectSingle

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def appView(request, pid, is_submited = False):
    userauth = {
        'role':"teacher",
    }
    return appManage(request, userauth, pid);    
    
@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def homeView(request):

    project_list = ProjectSingle.objects.all();
    context = {
        'project_list':project_list,

    }
    return render(request,"teacher/project_info.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def memberChange(request):
    professional=PROFESSIONAL_TITLE
    executive=EXECUTIVE_POSITION
    context={}
    context['professional']=professional
    context['executive']=executive
    return render(request,"teacher/member_change.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def commitmentView(request):
    context = {}
    return render(request, "teacher/commitment.html", context)


@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def finalReportView(request):
    context = finalReportViewWork(request)
    if context['redirect']:
		return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"teacher/final.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def progressReportView(request):
    context = {}
    return render(request,"teacher/progress.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def fileView(request):
    data={};
    return render(request,"teacher/file_upload.html",data)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def settingView(request):
    message = ""
    teacher = TeacherProfile.objects.get(userid = request.user)
    setting = TeacherInfoSetting.objects.get(teacher = teacher)
    if request.method == "GET":
        form = SettingForm(instance = setting)
    else:
        form = SettingForm(request.POST, instance = setting)
        if form.is_valid():
            form.save()
            message = "ok"
    context = {"form": form,
               "message": message,
               }
    return render(request, "teacher/setting.html", context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def financialView(request):
    if request.method == "POST":
        budgetinfoform = ProjectBudgetInformationForm(request.POST)
        budgetannuform = ProjectBudgetAnnualForm(request.POST)
        if budgetinfoform.is_valid():
            budgetinfo = budgetinfoform.cleaned_data
            print budgetinfo['project_basicexpenses']
    else:
        budgetinfoform = ProjectBudgetInformationForm()
        budgetannuform = ProjectBudgetAnnualForm()

    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"teacher/financial.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def finalInfoView(request):
    teacher = TeacherProfile.objects.get(userid = request.user)
    project_list = ProjectSingle.objects.filter(teacher = teacher)
    context = {
		'project_list':project_list,
    }
    return render(request,"teacher/finalinfo.html",context)

def fundBudgetView(request,pid):
    context = fundBudgetViewWork(request,pid)
    if context['redirect']:
		return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"teacher/fundbudget.html",context)
