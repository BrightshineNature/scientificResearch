# coding: UTF-8

from django.shortcuts import render
from common.forms import ScheduleForm, ScheduleBaseForm
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

