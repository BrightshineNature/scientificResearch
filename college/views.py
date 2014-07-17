# coding: UTF-8
'''
Created on 2014-06-07

Desc: college' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm


from college.forms import TeacherDispatchForm
def appView(request):
    context = {}
    return render(request, "college/application.html", context)
def scheduleView(request):
    userauth = {
                "role": 'college',
                }

    return scheduleManage(request, userauth,{})

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
    return render(request,"school/final.html",context)
def researchConcludingView(request):
    context={}
    return render(request,"college/research_concluding_view.html",context)
def dispatchView(request):
    teacher_form = TeacherDispatchForm()
    context = {
        "teacher_form": teacher_form,
    }
    return render(request, "college/dispatch.html", context)
