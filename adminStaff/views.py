# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage

def scheduleView(request):


    userauth = {
        'role': 'adminStaff',
    }


    return scheduleManage(request, userauth)
