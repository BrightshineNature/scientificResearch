# coding: UTF-8
'''
Created on 2014-06-07

Desc: school' view, includes home(manage), review report view
'''
from django.shortcuts import render
import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from backend.logging import loginfo
from backend.utility import getContext
from const import *
from common.utils import status_confirm,APPLICATION_SCHOOL_CONFIRM, getProjectReviewStatus 
from adminStaff.utility import getSpecial

from common.views import scheduleManage, researchConcludingManage,noticeMessageSettingBase, get_project_list, finalReportViewWork, appManage, fileUploadManage

from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm,SettingForm
from adminStaff.models import ProjectSingle, Re_Project_Expert
from school.forms import FilterForm,ExpertReviewForm
from adminStaff.forms import DispatchAddCollegeForm
from users.models import ExpertProfile, SchoolProfile,TeacherProfile
from common.forms import ScheduleBaseForm,EmailForm, SearchForm
from django.template.loader import render_to_string
from django.contrib.sites.models import get_current_site,Site

from school.forms import ExpertFinalReviewForm
@csrf.csrf_protect
@login_required
@check_submit_status()
def appView(request, pid, is_submited ):
    context = appManage(request, pid, is_submited)
    context['is_submited'] = is_submited[SUBMIT_STATUS_APPLICATION]
    context['user'] = "school"
    return render(request, "school/application.html", context)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def scheduleView(request):
    userauth = {
                "role": "school",
                "status":"application"
    }
    return scheduleManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"school/project_financial_info.html",context)


@csrf.csrf_protect
@login_required
@check_submit_status()
def finalReportView(request,pid,is_submited):
    context = finalReportViewWork(request,pid,is_submited[SUBMIT_STATUS_FINAL])
    context = dict(context, **fileUploadManage(request, pid, is_submited))
    context['is_submited'] = is_submited
    context['user'] = "special"
    loginfo(p=is_submited,label="is_submited")
    if context['redirect']:
		return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"school/final.html",context)


@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def progressReportView(requset):
    context={}
    return render(requset,"school/progress.html",context)
    
@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def allocView(request):
    expert_list = ExpertProfile.objects.all()
    unalloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    alloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    form = FilterForm(request = request)
    expert_form = FilterForm()
    
    context = {"form": form,
               "expert_form": expert_form,
               "page_info": "alloc",}
    context.update(getContext(unalloc_project_list, 1, "item", 0))
    context.update(getContext(alloc_project_list, 1, "item2", 0))
    context.update(getContext(expert_list, 1, "item3", 0))
    
    for expert in context['item3_list']:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True) & Q(project__project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)).count()

    for project in context['item2_list']:
        project.review_status = getProjectReviewStatus(project)


    return render(request, "school/alloc.html", context)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def researchConcludingView(request):
    userauth={
        "role":"school",
        "status":"research_concluding",
    }
    return researchConcludingManage(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def finalAllocView(request):
    expert_list = ExpertProfile.objects.all()
    unalloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_SCHOOL_OVER)
    alloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT)
    form = FilterForm(request = request)
    expert_form = FilterForm()
    context = {"form": form,
               "expert_form": expert_form,
               "page_info": "finalalloc",}
 
    context.update(getContext(unalloc_project_list, 1, "item", 0))
    context.update(getContext(alloc_project_list, 1, "item2", 0))
    context.update(getContext(expert_list, 1, "item3", 0))
    for expert in context['item3_list']:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True) & Q(project__project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)).count()

    for project in context['item2_list']:
        project.review_status = getProjectReviewStatus(project)

    return render(request, "school/alloc.html", context)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def noticeMessageSettingView(request):
    userauth={
        "role":"school"
    }
    return noticeMessageSettingBase(request,userauth)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def dispatchView(request):
    dispatchAddCollege_form=DispatchAddCollegeForm()
    try:
        teacher_users = TeacherProfile.objects.all().order_by('college')
    except:
        teacher_users = TeacherProfile.objects.none()
    context = {
               "dispatchAddCollege_form":dispatchAddCollege_form,
               "search_form": SearchForm(),
    }
    context.update(getContext(teacher_users, 1, "item"))
    return render(request, "school/dispatch.html", context)

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def controlView(request):
    expert_review_forms=[]
    expert_final_review_forms = []
    schedule_form=ScheduleBaseForm(request=request)
    specials =  getSpecial(request)
    for special in specials:
        expert_review_form = ExpertReviewForm(instance=special)
        expert_review_forms.append(expert_review_form)

        expert_final_review_forms.append(  ExpertFinalReviewForm(instance = special))

        control_types = []
        for t in CONTROL_TYPE_CHOICES:
            t = list(t)
            t.append(getattr(special,t[0]+"_status"))
            control_types.append(t)
        special.control_types = control_types

    # spec_list = zip(specials,expert_review_forms)
    spec_list = zip(specials,expert_review_forms, expert_final_review_forms)
    context = {
        'spec_list' :spec_list,
        'alloc_excel':TYPE_ALLOC[0],
        'final_alloc_excel':TYPE_FINAL_ALLOC[0],
        'schedule_form':schedule_form,
    }
    return render(request, "school/control.html", context);

@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def infoExportView(request):
    schedule_form = ScheduleBaseForm(request=request)
    context={'schedule_form':schedule_form,
             'EXCELTYPE_DICT':EXCELTYPE_DICT_OBJECT(),
            }
    return render(request,"school/exportExcel.html",context)
@csrf.csrf_protect
@login_required
@authority_required(SCHOOL_USER)
def allocEmailView(request,param):
    current_site = Site.objects.get_current()
    site_domain =current_site.domain
    email_form=EmailForm(request=request,initial={'mail_content':render_to_string('email/email_expert_content.txt',{'site':site_domain,
        'year':datetime.datetime.today().year,}),'mail_title':u'大连理工大学基本科研业务经费管理平台专家评审通知'})
    context = {
        "email_form":email_form,
        "param":param,
    }
    return render(request,"school/allocEmail.html",context)
