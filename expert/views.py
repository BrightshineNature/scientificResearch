# coding: UTF-8
'''
Created on 2014-06-07

Desc: expert' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm

def homeView(request):
    context={}
    return render(request,"expert/home.html",context)

def finalReportView(request):
    context = {}
    return render(request,"expert/final.html",context)

def applicationView(request):
    project_info_form = ProjectInfoForm()
    basis_content_form = BasisContentForm()
    base_condition_form = BaseConditionForm()
    context = {
        'project_info_form': project_info_form,
        'basis_content_form':basis_content_form,
        'base_condition_form':base_condition_form,
    }

    return render(request, "expert/application.html", context)
