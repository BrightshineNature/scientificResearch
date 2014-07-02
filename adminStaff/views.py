# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from common.forms import ScheduleForm
from common.views import scheduleManage

from adminStaff.forms import NewsForm, SchoolDispatchForm, CollegeDispatchForm, ExpertDispatchForm
def scheduleView(request):


    userauth = {
        'role': 'adminStaff',
    }


    return scheduleManage(request, userauth)
def newsRelease(request):
    context={}
    context.update({"newsform":NewsForm})
    return render(request,"adminStaff/news_release.html",context)
def noticeMessageSetting(request):
    context={}
    return render(request,"adminStaff/notice_message_setting.html",context)

def dispatchView(request):
    school_form = SchoolDispatchForm()
    college_form = CollegeDispatchForm()
    expert_form = ExpertDispatchForm()
    context = {"school_form": school_form, 
               "college_form": college_form, 
               "expert_form": expert_form, 
    }
    return render(request, "adminStaff/dispatch.html", context)
