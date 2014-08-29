# coding: UTF-8
'''
Created on 2014-06-07 by hujun

Desc: expert' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *

from adminStaff.models import Re_Project_Expert
from users.models import ExpertProfile
from backend.utility import getContext
from expert import forms
from common.utils import getScoreTable, getScoreForm
from teacher.forms import *
from teacher.models import *
from common.views import finalReportViewWork, appManage

@csrf.csrf_protect
@login_required
@authority_required(EXPERT_USER)
@check_submit_status(SUBMIT_STATUS_REVIEW)
def homeView(request, is_submited=False):
    is_first_round = request.GET.get("is_first_round", "1")
    expert = ExpertProfile.objects.get(userid = request.user)
    re_list_1 = list(Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True)))
    for re_obj in re_list_1:
        re_obj.score = getScoreTable(re_obj.project).objects.get(re_obj = re_obj).get_total_score()

    re_list_2 = list(Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = False)))
    for re_obj in re_list_2:
        re_obj.score = getScoreTable(re_obj.project).objects.get(re_obj = re_obj).get_total_score()
    context = {"is_first_round": is_first_round,}
    re_list_1.sort(key = lambda x: x.score)
    re_list_2.sort(key = lambda x: x.score)
    context.update(getContext(re_list_1, 1, "item", 0))
    context.update(getContext(re_list_2, 1, "item2", 0))

    return render(request,"expert/home.html", context)

@csrf.csrf_protect
@login_required
@authority_required(EXPERT_USER)
@check_submit_status(SUBMIT_STATUS_FINAL)
def finalReportView(request, is_submited = False):
    re_id = request.GET.get("re_id")
    re_obj = Re_Project_Expert.objects.get(id = re_id)
    pid = re_obj.project
    score_table = getScoreTable(re_obj.project).objects.get(re_obj = re_obj)
    
    context = finalReportViewWork(request, pid, is_submited)
    if request.method == "GET":
        score_form = getScoreForm(re_obj.project)(instance = score_table)

        context.update({
            'score_form': score_form,
            're_obj': re_obj,
        })
        return render(request,"expert/final.html",context)
    else:
        score_form = getScoreForm(re_obj.project)(request.POST, instance = score_table)
        if score_form.is_valid():
            score_form.save()
            return HttpResponseRedirect("/expert/redirect/?is_first_round=0")
        else:
            context.update({
                'score_form': score_form,
                're_obj': re_obj,
                'error': score_form.errors,
            })
            return render(request,"expert/final.html",context)

@csrf.csrf_protect
@login_required
@authority_required(EXPERT_USER)
@check_submit_status(SUBMIT_STATUS_APPLICATION)
def applicationView(request, is_submited = False):
    re_id = request.GET.get("re_id")
    re_obj = Re_Project_Expert.objects.get(id = re_id)
    pid = re_obj.project.project_id
    score_table = getScoreTable(re_obj.project).objects.get(re_obj = re_obj)

    context = appManage(request, pid)

    if request.method == "GET":
        score_form = getScoreForm(re_obj.project)(instance = score_table)
        context.update({
            'score_form': score_form,
            're_obj': re_obj,
        })
        return render(request, "expert/application.html", context)
    else:
        score_form = getScoreForm(re_obj.project)(request.POST, instance = score_table)
        if score_form.is_valid():
            score_form.save()
            return HttpResponseRedirect("/expert/redirect/?is_first_round=1")
        else:
            context.update({
                'score_form': score_form,
                're_obj': re_obj,
                'error': score_form.errors
            })
            return render(request, "expert/application.html", context)

