# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.views import  financeManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

def applicationProjectView(request):
    userauth={
        "role":"finance",
        "status":"budget"
    }
    return financeManage(request,userauth)

def concludingProjectView(request):
    userauth={
        "role":"finance",
        "status":"final",
    }
    return financeManage(request,userauth)

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
    return financeManage(request, userauth)


def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"finance/project_financial_info.html",context)
