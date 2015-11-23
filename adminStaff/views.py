# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
import time
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from backend.decorators import *
from const import *
from backend.logging import loginfo
from backend.utility import getContext

from adminStaff.forms import NewsForm,ObjectForm,TemplateNoticeMessageForm,DispatchForm,DispatchAddCollegeForm
from teacher.forms import ProjectBudgetInformationForm,ProjectBudgetAnnualForm, SettingForm, ProjectCreationTeacherForm
from common.forms import NoticeForm, SearchForm

from common.views import scheduleManage, financialManage,noticeMessageSettingBase,scheduleManage,finalReportViewWork,fundBudgetViewWork,fileUploadManage,researchConcludingManage,getType

from adminStaff.models import TemplateNoticeMessage,News,ProjectSingle,HomePagePic
from users.models import SchoolProfile,CollegeProfile,ExpertProfile,Special,College

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def appView(request):

    context = {}
    return render(request, "adminStaff/application.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def allocManageView(request):
    userauth = {
        'role': 'adminStaff',
    }
    object_form = ObjectForm()

    #special
    special_list = []
    user_special_info = {}
    for i in Special.objects.all() :
        special_list.append({'name':i.name, 'user':i.school_user, })

    for i in SchoolProfile.objects.all():
        user_special_info[i] = []
    for i in special_list:
        if i['user']:
            user_special_info[i['user']].append(i['name'])
    # college
    college_list = []
    user_college_info = {}
    for i in College.objects.all() :
        college_list.append({'name':i.name, 'user':i.college_user, })
    for i in CollegeProfile.objects.all():
        user_college_info[i] = []
    for i in college_list:
        if i['user']:
            user_college_info[i['user']].append(i['name'])
    instance_list = [ 
        {
            'object_chinese_name':"专题",
            'object_name': "special",
            'object_form': object_form,
            'object_list': special_list,
            'user_object_info':user_special_info,
        },
        {
            'object_chinese_name':"学院",
            'object_name': "college",
            'object_form': object_form,
            'object_list': college_list,
            'user_object_info':user_college_info,
        },
    ]
    context = { 
    'instance_list': instance_list,
    }
    return render(request, "adminStaff/alloc_manage.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def scheduleView(request):
    userauth = {
        'role': 'adminStaff',
        'status':'all'
    }
    return scheduleManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def deleteProject(request):
    try:
        iid=request.GET['iid']
        print iid
        project=ProjectSingle.objects.get(project_id=iid)
        if project:
            project.delete()
            return HttpResponse('Success')
        else:
            return HttpResponse('Not exists')
    except:
        return HttpResponse('Invalid project_id')


@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def newsRelease(request):
    if request.method == "GET":
        form = NewsForm()
    else:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    newsList = News.objects.all().order_by('-news_date')
    context = getContext(newsList,1,"item",page_elems=7)
    context.update({"newsform":NewsForm,
                  })
    return render(request,"adminStaff/news_release.html",context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def noticeMessageSetting(request):
    userauth={
        "role":"adminStaff"
    }
    return noticeMessageSettingBase(request,userauth)
def dispatchView(request):
    dispatch_form = DispatchForm()
    dispatchAddCollege_form=DispatchAddCollegeForm()
    college_users = CollegeProfile.objects.all()
    expert_users = ExpertProfile.objects.all().order_by('college')
    school_users = SchoolProfile.objects.all()
    context = {
               "dispatch_form":dispatch_form,
               "dispatchAddCollege_form":dispatchAddCollege_form,
               "search_form": SearchForm(),
    }
    context.update(getContext(school_users, 1, "item"))
    context.update(getContext(college_users, 1, "item2"))
    context.update(getContext(expert_users, 1, "item3"))
    return render(request, "adminStaff/dispatch.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def financialView(request):
    userauth = {
                "role": 'adminStaff', 
    }
    return financialManage(request, userauth)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def financialInfoView(request):
    budgetinfoform = ProjectBudgetInformationForm()
    budgetannuform = ProjectBudgetAnnualForm()    
    context = {
        'budgetinfoform':budgetinfoform,
        'budgetannuform':budgetannuform,
    }
    return render(request,"adminStaff/project_financial_info.html",context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def infoModifyView(request):
    context = {}
    return render(request, "adminStaff/teacher_info_modify.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def infoExportView(request):
    context = {
		'EXCELTYPE_DICT':EXCELTYPE_DICT_OBJECT(),
	}
    return render(request, "adminStaff/infoexport.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def finalInfoView(request,pid):
    project = ProjectSingle.objects.filter(project_id = pid)
    context = {
        'project_list':project,
        'role':'adminStaff',
    }
    return render(request, "adminStaff/finalinfo.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
@check_submit_status()
def finalReportView(request,pid,is_submited={}):
    print "YYA" * 10
    context = finalReportViewWork(request,pid,is_submited[SUBMIT_STATUS_FINAL])
    context = dict(context, **fileUploadManage(request, pid,is_submited))
    context['is_submited'] = is_submited
    context['user'] = "adminStaff"
    loginfo(p=is_submited,label="is_submited")
    # if context['redirect']:
    #     return HttpResponseRedirect('/teacher/finalinfo')
    return render(request,"adminStaff/final.html",context)
# def fileUploadManageView(request, pid, is_submited = False):

#     context = fileUploadManage(request, pid)
#     context['user'] = "teacher"
#     # is_submited = False
#     context['is_submited'] = is_submited

#     return render(request, "teacher/file_upload.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
@check_submit_status()
def fundBudgetView(request,pid,is_submited={}):
    context = fundBudgetViewWork(request,pid,is_submited[SUBMIT_STATUS_FINAL])
    context['role'] = 'adminStaff'
    if context['redirect']:
        return HttpResponseRedirect('/adminStaff/finalinfo/'+str(pid))
    return render(request,"adminStaff/fundbudget.html",context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
@check_submit_status()
def fileUploadManageView(request, pid, is_submited={}):

    context = fileUploadManage(request, pid, is_submited)
    context['user'] = "adminStaff"
    # is_submited = False
    context['is_submited'] = is_submited

    return render(request, "adminStaff/file_upload.html", context)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def homepic_import_view(request):
    """
    project group member change
    """
    if request.method == "POST":
        f = request.FILES["file"]
        ftype = getType(f.name)

        new_pic = HomePagePic()
        new_pic.pic_obj = f
        new_pic.name = f.name
        new_pic.file_type = ftype
        new_pic.uploadtime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
        new_pic.file_size = f.size
        new_pic.save()
    file_history = HomePagePic.objects.all()
    loginfo(file_history.count())
    data = {'files': file_history,
    }
    return render(request, 'adminStaff/home_pic_import.html', data)

@csrf.csrf_protect
@login_required
@authority_required(ADMINSTAFF_USER)
def createProject(request):
    """
    project group member change
    """
    return render(request, 'adminStaff/create_project.html', {'form': ProjectCreationTeacherForm()})
    
