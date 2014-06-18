# coding: UTF-8
'''
Created on 2014-06-07

Desc: school' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage
def scheduleView(request):

    userauth = {
                "role": 'school',                
    }
    return scheduleManage(request, userauth)



def final_report_view(request):
    context = {}
    return render(request,"school/final.html",context)
