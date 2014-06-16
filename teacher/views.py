# coding: UTF-8
'''
Created on 2014-06-07

Desc: teacher' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.views import scheduleManage
def homeView(request):


    context = {


    }
    return render(request,"teacher/project_info.html",context)

def final_report_view(request):
    context = {}
    return render(request,"teacher/final.html",context)
