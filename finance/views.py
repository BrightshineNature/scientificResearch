# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.views import scheduleManage, financialManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm

def homeView(request):

    context={}
    return render(request,"finance/home.html",context)

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
