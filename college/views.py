# coding: UTF-8
'''
Created on 2014-06-07

Desc: college' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from backend.logging import loginfo
from django.db.models import Q
from const import *
from backend.utility import getContext

from adminStaff.utility import getCollege
from common.views import scheduleManage, financialManage,researchConcludingManage,finalReportViewWork,fundBudgetViewWork,fileUploadManage
from adminStaff.utility import getCollege
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from adminStaff.forms import DispatchAddCollegeForm
from college.forms import TeacherDispatchForm

from users.models import TeacherProfile
from adminStaff.models import ProjectSingle


@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def appView(request):
    context = {}
    return render(request, "college/application.html", context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def scheduleView(request):
    userauth = {
            "role": 'college',
            "status":"application"  
                }

    return scheduleManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def financialView(request):
    userauth = {
                "role": 'college',                
    }
    return financialManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"college/project_financial_info.html",context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def finalReportView(request):
    context = {}
    return render(request,"college/final.html",context)
def researchConcludingView(request):
    userauth={
        'role':'college',
        'status':'research_concluding',
    }
    return researchConcludingManage(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def dispatchView(request):
    dispatchAddCollege_form=DispatchAddCollegeForm(user=request.user)
    colleges = getCollege(request)
    qset = reduce(lambda x,y:x|y,[Q(college = _college) for _college in colleges])
    teacher_users = TeacherProfile.objects.filter(qset)
    context = {
               "dispatchAddCollege_form":dispatchAddCollege_form,
    }
    context.update(getContext(teacher_users, 1, "item"))
    return render(request, "college/dispatch.html", context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def financialView(request):
    userauth = {
                "role": 'adminStaff', 
    }
    return financialManage(request, userauth)
    teacher_form = TeacherDispatchForm()
    context = {
        "teacher_form": teacher_form,
    }
    return render(request, "college/dispatch.html", context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
def finalInfoView(request,pid):
    project = ProjectSingle.objects.filter(project_id = pid)
    context = {
        'project_list':project,
        'role':'college',
    }
    return render(request, "college/finalinfo.html", context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
@check_submit_status(SUBMIT_STATUS_FINAL)
def finalReportView(request,pid,is_submited=False):
    context = finalReportViewWork(request,pid,is_submited)
    loginfo(p=is_submited,label="is_submited")
    # if context['redirect']:
    #     return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"college/final.html",context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
@check_submit_status(SUBMIT_STATUS_FINAL)
def fundBudgetView(request,pid,is_submited=False):
    context = fundBudgetViewWork(request,pid,is_submited)
    context['role'] = 'college'
    if context['redirect']:
        return HttpResponseRedirect('/college/finalinfo/'+str(pid))
    return render(request,"college/fundbudget.html",context)

@csrf.csrf_protect
@login_required
@authority_required(COLLEGE_USER)
@check_submit_status(SUBMIT_STATUS_APPLICATION)
def fileUploadManageView(request, pid, is_submited = False):
    print "haha"*100
    context = fileUploadManage(request, pid)
    context['user'] = "college"
    # is_submited = False
    context['is_submited'] = is_submited
    loginfo(p=context['files'],label="files")
    return render(request, "college/file_upload.html", context)
