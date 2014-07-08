# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

def applicationProjectView(request):
    context={}
    return render(request,"finance/applicationProject.html",context)

def concludingProjectView(request):
    context={}
    return render(request,"finance/concludingProject.html",context)

def financeBudgetView(request):
    context={}
    return render(request,"finance/financeBudget.html",context)

def financeAuditingView(request):
    context={}
    return render(request,"finance/financeAuditing.html",context)

def financialView(request):
    userauth = {
                "role": 'finance', 
    }
    return financialManage(request, userauth)


def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"finance/project_financial_info.html",context)
