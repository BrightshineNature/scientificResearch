# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from backend.logging import loginfo
from const import *

from common.views import  financeManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def applicationProjectView(request):
    userauth={
        "role":"finance",
        "status":"budget"
    }
    return financeManage(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def concludingProjectView(request):
    userauth={
        "role":"finance",
        "status":"final",
    }
    return financeManage(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def financeBudgetView(request):
    context={}
    return render(request,"finance/financeBudget.html",context)

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def financeAuditingView(request):
    context={}
    return render(request,"finance/financeAuditing.html",context)

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def financialView(request):
    userauth = {
                "role": 'finance', 
    }
    return financeManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"finance/project_financial_info.html",context)
