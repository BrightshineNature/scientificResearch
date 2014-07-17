# coding: UTF-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from common.forms import ScheduleForm, ScheduleBaseForm
from const import *
from teacher.forms import *
from teacher.models import *
from backend.logging import logger, loginfo
def scheduleManage(request, userauth):

    context = schedule_form_data(request, userauth)

    return render(request, userauth['role'] + '/schedule.html', context)

def financialManage(request, userauth):
    
    context = schedule_form_data(request, userauth)

    return render(request, userauth['role'] + '/financial.html', context)

def schedule_form_data(request , userauth):

    if userauth['role'] == 'college':
        schedule_form = ScheduleBaseForm()
    else :
        schedule_form = ScheduleForm()
    
    has_data = False
    if request.method == 'POST':
        if userauth['role'] == 'college':
            schedule_form = ScheduleBaseForm(request.POST)
        else :
            schedule_form = ScheduleForm(request.POST)

        if schedule_form.is_valid():
            print schedule_form.cleaned_data['status']
            print schedule_form.cleaned_data['year']
            print schedule_form.cleaned_data['special']
            if userauth['role'] != 'college':
                print schedule_form.cleaned_data['college']
            print schedule_form.cleaned_data['teacher_name']
            has_data = True



    
    context ={ 'schedule_form':schedule_form,
               'has_data': has_data,
               'userauth': userauth,
    }

    return context

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
