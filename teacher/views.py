# coding: UTF-8
'''
Created on 2014-06-07

Desc: teacher' view, includes home(manage), review report view
'''
from django.shortcuts import render
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
def homeView(request):
    context={}
    return render(request,"teacher/home.html",context)
def memberChange(request):
    context={}
    return render(request,"teacher/member_change.html",context)

def final_report_view(request):
    context = {}
    return render(request,"teacher/final.html",context)

def financial_view(request):
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
