# coding: UTF-8
'''
Created on 2014-06-07

Desc: school' view, includes home(manage), review report view
'''
from django.shortcuts import render
from django.db.models import Q

from common.views import scheduleManage, financialManage,researchConcludingManage
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm
from teacher.forms import SettingForm
from adminStaff.models import ProjectSingle, Re_Project_Expert
from users.models import ExpertProfile
from school.forms import CollegeForm
from backend.utility import getContext

def appView(request):
    context = {}
    return render(request,"school/application.html",context)
def scheduleView(request):

    userauth = {
                "role": "school",
                "status":"application"
    }
    return scheduleManage(request, userauth)


def financialView(request):
    userauth = {
                "role": 'school',                
    }
    return financialManage(request, userauth)


def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"school/project_financial_info.html",context)

def finalReportView(request):
    context = {}
    return render(request,"school/final.html",context)
def progressReportView(requset):
    context={}
    return render(requset,"school/progress.html",context)

def allocView(request):
    if request.method == "GET":
        project_list = ProjectSingle.objects.all()

        expert_list = ExpertProfile.objects.all()
    
        college_form = CollegeForm()
    else:
        college_form = CollegeForm(request.POST)
        if college_form.is_valid():
            college = college_form.cleaned_data["colleges"]
            if college == "-1":
                project_list = ProjectSingle.objects.all()
                expert_list = ExpertProfile.objects.all()
            else:
                project_list = ProjectSingle.objects.filter(teacher__college = college)
                expert_list = ExpertProfile.objects.filter(college = college)

    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True)).count()
    
    context = getContext(project_list, 1, "item", 0)
    context.update({
                    "expert_list": expert_list,
                    "college_form": college_form,
                  })
    return render(request, "school/alloc.html", context)

def researchConcludingView(request):
    userauth={
        "role":"school",
        "status":"research_concluding",
    }
    return researchConcludingManage(request,userauth)

def finalAllocView(request):
    context = {}
    return render(request, "school/final_alloc.html", context)
def noticeMessageSettingView(request):
    context = {}
    return render(request, "school/notice.html", context)

def controlView(request):
    

    special = [     
              {
                'year_list': [2015,],
                'special_name': 'science',
    },
              {
                'year_list': [2011,2012,2013,2014,],
                'special_name': 'liberal',
    },
        
    ]


    
    context = {
        'special' :special,
    }
    return render(request, "school/control.html", context);

def infoModifyView(request):
    form = SettingForm()
    context = {"form": form,}
    return render(request, "school/teacher_info_modify.html", context)
