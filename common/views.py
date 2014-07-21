# coding: UTF-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from common.forms import  ScheduleBaseForm
from common.utils import get_query_status,get_qset,get_query_application_status
from const import *
from teacher.forms import *
from teacher.models import *
from backend.logging import logger, loginfo
from adminStaff.models import ProjectSingle
from django.db.models import Q

    
def getParam(pro_list, userauth,flag):
    (pending_q,default_q,search_q)=get_qset(userauth)
    not_pass_apply_project_group=pro_list.filter(pending_q)
    if flag:
        pass_apply_project_group=pro_list.filter(default_q)
    else:
        pass_apply_project_group=pro_list.filter(search_q)
    count=not_pass_apply_project_group.count()+pass_apply_project_group.count()
    param={
        "not_pass_apply_project_group":not_pass_apply_project_group,
        "pass_apply_project_group":pass_apply_project_group,
        "total_count":count,
    }
    return param

def scheduleManage(request, userauth):
    context = schedule_form_data(request, userauth)
    return render(request, userauth['role'] + '/schedule.html', context)
def researchConcludingManage(request , userauth):
    context = schedule_form_data(request , userauth)
    return render(request, userauth['role']+'/research_concluding.html' ,context)
def financialManage(request, userauth):
    
    context = schedule_form_data(request, userauth)

    return render(request, userauth['role'] + '/financial.html', context)

def schedule_form_data(request , userauth):

    schedule_form = ScheduleBaseForm()
    
    
    has_data = False
    if request.method == 'POST':
        
        schedule_form = ScheduleBaseForm(request.POST)
        pro_list=get_search_data(schedule_form)
        default=False
    else:
        pro_list=ProjectSingle.objects.all()
        default=True
    param=getParam(pro_list,userauth,default)
    context ={ 'schedule_form':schedule_form,
               'has_data': has_data,
               'userauth': userauth,
    }
    
    context.update(param)

    return context
def get_search_data(schedule_form):
     if schedule_form.is_valid():
            application_status=schedule_form.cleaned_data['application_status']
            status=schedule_form.cleaned_data['status']
            application_year= schedule_form.cleaned_data['application_year']
            approval_year=schedule_form.cleaned_data['approval_year']
            special=schedule_form.cleaned_data['special']
            college=schedule_form.cleaned_data['college']
            other_search=schedule_form.cleaned_data['other_search']
            if application_status=="-1":
                application_status=''
            elif application_status:
                (application_first_status,application_last_status)=get_query_application_status(application_status)
            if status=="-1":
                status=''
            elif status:
                (first_status,last_status)=get_query_status(status)
            if application_year=="-1":
                application_year=''
            if approval_year=="-1":
                approval_year=''
            if special=="-1":
                special=''
            if college=="-1":
                college=''
            q0=(application_status and Q(project_status__status__gte=application_first_status,project_status__status__lte=application_last_status)) or None
            q1=(status and Q(project_status__status__gte=first_status,project_status__lte=last_status)) or None
            q2=(application_year and Q(application_year=application_year)) or None
            q3=(approval_year and Q(approval_year=approval_year)) or None
            q4=(special and Q(project_special=special)) or None
            q5=(college and Q(school=college)) or None
            if other_search:
                sqlstr=other_search
                q6_1=Q(project_code__contains=sqlstr)
                q6_2=Q(project_application_code__contains=sqlstr)
                q6_3=Q(title__contains=sqlstr)
                q6_4=Q(teacher__teacherinfosetting__name__contains=sqlstr)
                q6=reduce(lambda x,y:x|y,[q6_1,q6_2,q6_3,q6_4])
            else:
                q6=None
            qset=filter(lambda x:x!=None,[q0,q1,q2,q3,q4,q5,q6])
            if qset:
                qset=reduce(lambda x,y: x&y ,qset)
                pro_list=ProjectSingle.objects.filter(qset)
            else:
                pro_list=ProjectSingle.objects.all()
            return pro_list


def finalReportViewWork(request,redirect=False):
    achivement_type = ACHIVEMENT_TYPE
    statics_type = STATICS_TYPE
    statics_grade_type = STATICS_PRIZE_TYPE

    final = FinalSubmit.objects.all()[0]
    achivement_list = ProjectAchivement.objects.filter(finalsubmit_id = final.content_id)
    projachivementform  = ProjectAchivementForm()

    for temp in achivement_list:
        loginfo(p=temp.achivementtype,label="achivementtype")

    if request.method == "POST":
        final_form = FinalReportForm(request.POST, instance=final)
        if final_form.is_valid():
            final_form.save()
            redirect = True
        else:
            logger.info("Final Form Valid Failed"+"**"*10)
            logger.info(final_form.errors)
    else:
        final_form = FinalReportForm(instance=final)


    context = {
        'projachivementform':projachivementform,
        'statics_type':statics_type,
        'statics_grade_type':statics_grade_type,
        'final': final_form,
        'finalreportid':final.content_id,
        'redirect':redirect,
        'achivement_list':achivement_list,

    }
    return context
