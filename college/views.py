# coding: UTF-8
'''
Created on 2014-06-07

Desc: college' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage

from college.forms import TeacherDispatchForm
def scheduleView(request):
    userauth = {
                "role": 'college',
                }

    return scheduleManage(request, userauth)


def final_report_view(request):
    context = {}
    return render(request,"school/final.html",context)

def dispatchView(request):
    teacher_form = TeacherDispatchForm()
    context = {
        "teacher_form": teacher_form,
    }

    return render(request, "college/dispatch.html", context)
