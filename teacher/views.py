# coding: UTF-8
'''
Created on 2014-06-07

Desc: teacher' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from const import * 
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm, SettingForm
from common.views import scheduleManage,finalReportViewWork
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm
from users.models import TeacherProfile
from teacher.models import TeacherInfoSetting
from common.views import appManage
from adminStaff.models import ProjectSingle
def appView(request, pid):

    userauth = {
        'role':"teacher",
    }
    return appManage(request, userauth, pid);    
    
def homeView(request):

    project_list = ProjectSingle.objects.all();
    context = {
        'project_list':project_list,

    }
    return render(request,"teacher/project_info.html",context)
def memberChange(request):
    professional=PROFESSIONAL_TITLE
    executive=EXECUTIVE_POSITION
    context={}
    context['professional']=professional
    context['executive']=executive
    return render(request,"teacher/member_change.html",context)

def commitmentView(request):
    context = {}
    return render(request, "teacher/commitment.html", context)

def finalReportView(request):

    context = finalReportViewWork(request)
    if context['redirect']:
		return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"teacher/final.html",context)

def progressReportView(request):
    context = {}
    return render(request,"teacher/progress.html",context)

def fileView(request):
    data={};
    return render(request,"teacher/file_upload.html",data)

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

def finalInfoView(request):

    context = {

    }
    return render(request,"teacher/finalinfo.html",context)
