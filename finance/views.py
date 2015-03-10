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

from common.views import  financeManage,fundBudgetViewWork,finalReportViewWork, appManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from common.forms import ScheduleBaseForm

@csrf.csrf_protect
@login_required
@check_submit_status()
def appView(request, pid, is_submited):
    context = appManage(request, pid, is_submited)
    context['is_submited'] = is_submited[SUBMIT_STATUS_APPLICATION]
    context['user'] = "finance"
    return render(request, "finance/application.html", context)

@csrf.csrf_protect
@login_required
@check_submit_status()
def finalReportView(request,pid,is_submited):
    context = finalReportViewWork(request,pid,is_submited[SUBMIT_STATUS_FINAL])
    return render(request,"finance/final.html",context)

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
def financeBudgetView(request,pid):
    context=fundBudgetViewWork(request,pid,False)
    return render(request,"finance/financeBudget.html",context)

@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def financeAuditingView(request,pid):
    context=finalReportViewWork(request,pid,False)
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
@csrf.csrf_protect
@login_required
@authority_required(FINANCE_USER)
def exportFinanceView(request):
    schedule_form = ScheduleBaseForm()
    context={'schedule_form':schedule_form,
             'EXCELTYPE_DICT':EXCELTYPE_DICT_OBJECT(),
            }
    return render(request,"finance/exportFinance.html",context)
