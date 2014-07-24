# coding: UTF-8
'''
Created on 2014-06-07

Desc: college' view, includes home(manage), review report view
'''
from django.shortcuts import render
from users.models import TeacherProfile
from common.views import scheduleManage, financialManage,researchConcludingManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from adminStaff.forms import DispatchAddCollegeForm

from college.forms import TeacherDispatchForm
def appView(request):
    context = {}
    return render(request, "college/application.html", context)
def scheduleView(request):
    userauth = {
            "role": 'college',
            "status":"application"  
                }

    return scheduleManage(request, userauth)

def financialView(request):
    userauth = {
                "role": 'college',                
    }
    return financialManage(request, userauth)


def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"college/project_financial_info.html",context)

def finalReportView(request):
    context = {}
    return render(request,"college/final.html",context)
def researchConcludingView(request):
    userauth={
        'role':'college',
        'status':'research_concluding',
    }
    return researchConcludingManage(request,userauth)
def dispatchView(request):
    dispatchAddCollege_form=DispatchAddCollegeForm()
    teacher_users = TeacherProfile.objects.all()
    context = {
               "dispatchAddCollege_form":dispatchAddCollege_form,
               "users":teacher_users,
    }
    return render(request, "college/dispatch.html", context)
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
