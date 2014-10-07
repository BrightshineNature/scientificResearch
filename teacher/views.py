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
from django.db.models import Q

from common.views import scheduleManage,finalReportViewWork,appManage,fundBudgetViewWork, fileUploadManage,get_project_list

from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm, SettingForm
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm

from users.models import TeacherProfile
from teacher.models import TeacherInfoSetting
from adminStaff.models import ProjectSingle
from forms import ProjectCreationForm
from common.utils import createNewProject
from common.views import get_project_list
from const import PROJECT_STATUS_APPLICATION_REVIEW_OVER

import datetime

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
@check_submit_status(SUBMIT_STATUS_APPLICATION)
def appView(request, pid, is_submited = False):
    userauth = {
        'role':"teacher",
    }
    
    context = appManage(request, pid)
    context['user'] = "teacher" 
    context['is_submited'] = is_submited
    context['is_submited'] = True
    return render(request, "teacher/application.html", context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
@check_submit_status(SUBMIT_STATUS_APPLICATION)
def fileUploadManageView(request, pid, is_submited = False):

    context = fileUploadManage(request, pid)
    context['user'] = "teacher"
    # is_submited = False
    context['is_submited'] = is_submited

    return render(request, "teacher/file_upload.html", context)

def firstLoginChecker(request):
    setting = TeacherInfoSetting.objects.get(teacher__userid = request.user)
    if setting.name == None:
        return False
    return True

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def homeView(request):
    if not firstLoginChecker(request):
        return HttpResponseRedirect(reverse("teacher.views.settingView"))

    project_list = get_project_list(request).filter(project_status__status__lt = PROJECT_STATUS_APPROVAL);
    year = datetime.datetime.now().year   
    projectCreationForbidCheck = (get_project_list(request).filter(Q(application_year = year) | Q(approval_year = year)).count() > 0)
    creationForm = ProjectCreationForm()
    comment=""
    for item in project_list:
        if item.comment!="":
            comment=item.comment
    context = {
        'comment':comment,
        'project_list':project_list,
        'form': creationForm,
        'projectCreationForbidCheck': projectCreationForbidCheck,
    }
    return render(request,"teacher/project_info.html",context)
@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def finalInfoView(request):
    project_list = get_project_list(request).filter(project_status__status__gte = PROJECT_STATUS_APPROVAL);
    context = {
		'project_list':project_list,
    }
    return render(request,"teacher/finalinfo.html",context)
@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def createView(request):
    if request.method == "POST":
        creationForm = ProjectCreationForm(request.POST)
        if creationForm.is_valid():
            title = creationForm.cleaned_data["title"]
            special = creationForm.cleaned_data["special"]
            teacher = TeacherProfile.objects.get(userid = request.user)
            createNewProject(teacher, title, special)
            return HttpResponseRedirect(reverse("teacher.views.homeView"))
        else:
            pass


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
@check_submit_status(SUBMIT_STATUS_FINAL)
def finalReportView(request,pid,is_submited=False):
    context = finalReportViewWork(request,pid,is_submited)
    loginfo(p=is_submited,label="is_submited")
    if context['redirect']:
		return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"teacher/final.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def progressReportView(request):
    context = {}
    return render(request,"teacher/progress.html",context)

# @csrf.csrf_protect
# @login_required
# @authority_required(TEACHER_USER)
# def fileView(request):
#     data={};
#     return render(request,"teacher/file_upload.html",data)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
def settingView(request):
    message = ""
    teacher = TeacherProfile.objects.get(userid = request.user)
    setting = TeacherInfoSetting.objects.get(teacher = teacher)
    is_first = firstLoginChecker(request)

    if request.method == "GET":
        setting.name = teacher.userid.first_name
        form = SettingForm(instance = setting)
    else:
        form = SettingForm(request.POST, instance = setting)
        if form.is_valid():
            form.save()
            is_first = True
            message = "ok"
    context = {"form": form,
               "message": message,
               "is_first": is_first,
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
    project_list = get_project_list(request).filter(project_status__status__gte=PROJECT_STATUS_APPLICATION_REVIEW_OVER)
    teacher = TeacherProfile.objects.get(userid = request.user)
    project_list = ProjectSingle.objects.filter(teacher = teacher).filter(project_status__status__gte = PROJECT_STATUS_APPROVAL )
    context = {
		'project_list':project_list,
        'role':'teacher',
    }
    return render(request,"teacher/finalinfo.html",context)

@csrf.csrf_protect
@login_required
@authority_required(TEACHER_USER)
@check_submit_status(SUBMIT_STATUS_TASK)
def fundBudgetView(request,pid,is_submited=False):
    context = fundBudgetViewWork(request,pid,is_submited)
    if context['redirect']:
		return HttpResponseRedirect('/teacher/finalinfo')
    context['role'] = 'teacher'
    return render(request,"teacher/fundbudget.html",context)
