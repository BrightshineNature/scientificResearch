# coding: UTF-8
'''
Created on 2014-06-07

Desc: expert' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm
from django.db.models import Q

from adminStaff.models import Re_Project_Expert
from users.models import ExpertProfile
from backend.utility import getContext

def homeView(request):
    expert = ExpertProfile.objects.get(userid = request.user)
    project_list_1 = [re_obj.project for re_obj in Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True))]
    project_list_2 = [re_obj.project for re_obj in Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = False))]
    context = {}

    context.update(getContext(project_list_1, 1, "item", 0, 2))
    context.update(getContext(project_list_2, 1, "item2", 0, 2))

    return render(request,"expert/home.html", context)

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
