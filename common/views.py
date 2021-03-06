# coding: UTF-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from common.forms import  ScheduleBaseForm,ProjectJudgeForm, ProjectMemberForm
from common.utils import get_query_status,get_qset,get_query_application_status,status_confirm
from common.utility import get_single_project_average_score
from const import *
from teacher.forms import *
from teacher.models import *
from backend.logging import logger, loginfo
from adminStaff.models import ProjectSingle,TemplateNoticeMessage
from django.db.models import Q
from backend.utility import getContext

from adminStaff.utility import getCollege,getSpecial
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm,NoticeForm,AllStatusForm
from adminStaff.forms import TemplateNoticeMessageForm
from const.models import ScienceActivityType
from teacher.models import ProjectFundBudget
from users.models import College,Special
from common.models import ProjectMember,BasisContent , BaseCondition, UploadFile
from dajaxice.utils import deserialize_form

import datetime

def getSingleProjectURLList(item):
    URLList = []
    if item.file_application:
        try:
            file_obj = UploadFile.objects.filter(project=item,file_type=FileList['file_application'])[0]
            URLList.append(file_obj)
        except:
            item.file_application=False
            URLList.append(None)
    if item.file_task:
        try:
            file_obj = UploadFile.objects.filter(project=item,file_type=FileList['file_task'])[0]
            URLList.append(file_obj)
        except:
            item.file_application=False
            URLList.append(None)
    if item.file_interimchecklist:
        try:
            file_obj = UploadFile.objects.filter(project=item,file_type=FileList['file_interimchecklist'])[0]
            URLList.append(file_obj)
        except:
            item.file_application=False
            URLList.append(None)
    if item.file_summary:
        try:
            file_obj = UploadFile.objects.filter(project=item,file_type=FileList['file_summary'])[0]
            URLList.append(file_obj)
        except:
            item.file_application=False
            URLList.append(None)

    return URLList

def addURL(project_list):
    for item in project_list:
        if item.file_application:
            try:
                item.application_url=UploadFile.objects.filter(project=item,file_type=FileList['file_application'])[0].file_obj.url
            except:
                item.file_application=False
        if item.file_task:
            try:
                item.task_url=UploadFile.objects.filter(project=item,file_type=FileList['file_task'])[0].file_obj.url
            except:
                item.file_task=False
        if item.file_interimchecklist:
            try:
                item.progress_url=UploadFile.objects.filter(project=item,file_type=FileList['file_interimchecklist']).order_by("-upload_time")[0].file_obj.url
            except:
                item.file_interimchecklist=False
        if item.file_summary:
            try:
                item.summary_url=UploadFile.objects.filter(project=item,file_type=FileList['file_summary'])[0].file_obj.url
            except:
                item.file_summary=False
    return project_list
def getParam(pro_list, userauth,flag,page,page2):
    (pending_q,default_q,search_q)=get_qset(userauth)
    not_pass_apply_project_group=pro_list.filter(pending_q)
    if flag:
        pass_apply_project_group=pro_list.filter(default_q)
    else:
        pass_apply_project_group=pro_list.filter(search_q)
    if userauth['role']==FINANCE_USER:
        if userauth['status']=="budget":
            pass_apply_project_group = pass_apply_project_group.order_by('projectfundbudget__serial_number')
        else:
            pass_apply_project_group = pass_apply_project_group.order_by('projectfundsummary__serial_number')
    pass_apply_project_group=addURL(pass_apply_project_group)
    not_pass_apply_project_group=addURL(not_pass_apply_project_group)
    param={}
    param.update(getContext(pass_apply_project_group,page2,"item2",0,page_elems=10))
    param.update(getContext(not_pass_apply_project_group,page,"item",0,page_elems=10))
    param.update({"pro_count":len(pass_apply_project_group)})
    return param

def appManage(request, pid, is_submited):
    page = request.GET.get('page')
    page2 = request.GET.get('page2')
    if page == None:
        page = 1
    if page2 == None:
        page2 = 1
    basis_content = BasisContent.objects.filter(project__project_id = pid)
    if basis_content:
        basis_content_id = basis_content[0].id
        basis_content_form = BasisContentForm(instance = basis_content[0])
    else :
        basis_content_id = ""
        basis_content_form = BasisContentForm()

    base_condition = BaseCondition.objects.filter(project__project_id = pid)
    if base_condition:
        base_condition_id = base_condition[0].id
        base_condition_form = BaseConditionForm(instance = base_condition[0])
    else :
        base_condition_id = ""
        base_condition_form = BaseConditionForm()

    p = ProjectSingle.objects.get(project_id = pid)
    project_info_data = { 
        'project_name': p.title,
        'science_type': p.science_type.category if p.science_type else '-1',
        'trade_code': p.trade_code.category if p.trade_code else '-1',
        'subject': p.subject.category if p.subject else '-1',
        'start_time': p.start_time,
        'end_time': p.end_time,
        'project_tpye': p.project_tpye,
    }
    project_member_list = ProjectMember.objects.filter(project__project_id = pid)
    context = {
        'project_info_form': ProjectInfoForm(project_info_data),
        'project_member_form': ProjectMemberForm(),
        'basis_content_form':basis_content_form,
        'basis_content_id':basis_content_id,
        'base_condition_form':base_condition_form,
        'base_condition_id':base_condition_id,
        'project_member_list': project_member_list,
        'pro':p,
        'pid': pid,
        'page':page,
        'page2':page2,
    }


    file_upload_context = fileUploadManage(request, pid, is_submited)
    context = dict(file_upload_context.items()+context.items())

    return context

from django.core.files.storage import default_storage
import time

def getType(fname):
    for i in FileList:
        if FileList[i] == fname.split('.')[0]:
            return FileList[i]
    return FileList['file_other']



AcceptedExtension = [
    'doc', 'docx', 'DOC', 'DOCX',
]
def handleFileUpload(request, pid,  entrance):
    f = request.FILES[entrance]
    ftype = getType(f.name)
    ftype = FileList[entrance]
    # if(ftype != FileList[entrance]):
    #     return 0
    obj = UploadFile() 
    if ftype != FileList['file_other']:
        if f.name.count('.') == 0: 
            return 0
        if not AcceptedExtension.count(f.name.split('.')[1]):
            return 0
        obj = UploadFile.objects.filter(project__project_id = pid, file_type = ftype)
    else:
        obj = UploadFile.objects.filter(project__project_id = pid, name = f.name)

    if entrance == "file_application" or \
    entrance == "file_task" or \
    entrance == "file_summary":
        for i in obj:
            path = i.file_obj.path
            i.delete()
            default_storage.delete(path)
    project = ProjectSingle.objects.get(project_id = pid)
    obj = UploadFile()
    obj.name = f.name
    obj.project = project
    obj.file_obj = f
    obj.upload_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    obj.file_type = ftype
    obj.file_size = f.size
    obj.save()
    timenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if entrance == 'file_application':
        project.file_application = True
        project.submit_date=timenow
        if project.project_status.status == PROJECT_STATUS_APPLICATION_WEB_OVER:
           status_confirm(request,project)
    elif entrance == 'file_task':
        project.file_task = True
        project.submit_date=timenow
        if project.project_status.status == PROJECT_STATUS_TASK_FINANCE_OVER:
           status_confirm(request,project)
    elif entrance == 'file_interimchecklist':
        project.file_interimchecklist = True
        project.submit_date=timenow
        if project.project_status.status == PROJECT_STATUS_PROGRESS_WEB_OVER:
           status_confirm(request,project)
    elif entrance == 'file_summary':
        project.file_summary = True
        project.submit_date=timenow
        if project.project_status.status == PROJECT_STATUS_FINAL_WEB_OVER:
           status_confirm(request,project)
    project.save()
    return 1

def fileUploadManage(request, pid, is_submited):
    error = 0
    is_upload_file = 0
    if request.method == 'POST':
        if request.POST.has_key("is_delete_file"):
            fid = request.POST['fid']
            deleted_file = UploadFile.objects.get(id = fid)
            path = deleted_file.file_obj.path
            deleted_file.delete()
            default_storage.delete(path)
            is_upload_file = 1
        else:
            for i in FileList:
                if request.FILES.has_key(i):
                    if not handleFileUpload(request, pid, i):
                        error = 1
                    else :
                        is_upload_file = 1
    else :
        pass
        # form = UploadFileForm()

    files = UploadFile.objects.filter(project__project_id = pid)
    loginfo(p=files,label="files")

    for i in files:
        i.file_size = '%.3f KB' % (float(i.file_size) / 1024)
        # i.file_size += 'KB'

    context = {
        'files': files,
        'upload_file_error': error, 
        'is_upload_file':is_upload_file,
        'is_can_submited':is_submited, 

    }
    return context

def scheduleManage(request, userauth):
    page = request.GET.get('page')
    page2 = request.GET.get('page2')
    if page == None:
        page = 1
    if page2 == None:
        page2 = 1
    context = schedule_form_data(request, userauth,page=page,page2=page2)
    if userauth['role']=="adminStaff":
        statusform=AllStatusForm()
        context.update({'allstatusform':statusform})
    return render(request, userauth['role'] + '/schedule.html', context)

def researchConcludingManage(request , userauth):
    page = request.GET.get('page')
    page2 = request.GET.get('page2')
    if page == None:
        page = 1
    if page2 == None:
        page2 = 1
    context = schedule_form_data(request , userauth,page=page,page2=page2)
    return render(request, userauth['role']+'/research_concluding.html' ,context)

def financeManage(request, userauth):
    page = request.GET.get('page')
    page2 = request.GET.get('page2')
    if page == None:
        page = 1
    if page2 == None:
        page2 = 1
    context = schedule_form_data(request, userauth,page=page,page2=page2)
    for item in context.get("item2_list"):
        item.remain=int(item.projectfundsummary.total_budget)-int(item.projectfundsummary.total_expenditure)
    for item in context.get("item_list"):
        item.remain=int(item.projectfundsummary.total_budget)-int(item.projectfundsummary.total_expenditure)
    return render(request, userauth['role'] + '/financeProject.html', context)

def financialManage(request, userauth):
    context = schedule_form_data(request, userauth)
    return render(request, userauth['role'] + '/financial.html', context)

def schedule_form_data(request ,userauth="" ,form="",page=1,page2=1,search=0):
    ProjectJudge_form=ProjectJudgeForm()
    has_data = False
    schedule_form=ScheduleBaseForm(request=request)
    if search == 1:
        schedule_form = ScheduleBaseForm(deserialize_form(form))
        pro_list=get_search_data(request,schedule_form)
        default=False
    else:
        pro_list=get_project_list(request)
        default=True
    param=getParam(pro_list,userauth,default,page,page2)
    context ={ 'schedule_form':schedule_form,
               'has_data': has_data,
               'usercontext': userauth,
               'ProjectJudge_form':ProjectJudge_form,
               "approve":PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,
               "review":PROJECT_STATUS_FINAL_EXPERT_SUBJECT,
               "page":page,
               "page2":page2,
               'EXCELTYPE_DICT':EXCELTYPE_DICT_OBJECT(),
    }
    if userauth['role']!="college" and userauth['role']!="adminStaff":
        context.update({'show':1})
    context.update(param)
    return context

def get_project_list(request):
    identity = request.session.get('auth_role', "")
    if identity == ADMINSTAFF_USER:
        pro_list = ProjectSingle.objects.all()
    elif identity == SCHOOL_USER:
        specials = getSpecial(request)
        try:
            qset = reduce(lambda x,y:x|y,[Q(project_special = _special) for _special in specials])
            pro_list = ProjectSingle.objects.filter(qset).order_by("project_code")
        except:
            pro_list = ProjectSingle.objects.none()
    elif identity == COLLEGE_USER:
        try:
            colleges = getCollege(request)
            qset = reduce(lambda x,y:x|y,[Q(teacher__college = _college) for _college in colleges])
            pro_list = ProjectSingle.objects.filter(qset)
        except:
            pro_list = ProjectSingle.objects.none()
    elif identity == TEACHER_USER:
        pro_list = ProjectSingle.objects.filter(teacher__userid = request.user)
    elif identity == EXPERT_USER:
        pro_list = ProjectSingle.objects.all()
    else:
        pro_list = ProjectSingle.objects.all()
    return pro_list
def get_search_data(request,schedule_form):
    if schedule_form.is_valid():
        application_status=schedule_form.cleaned_data['application_status']
        status=schedule_form.cleaned_data['status']
        application_year= schedule_form.cleaned_data['application_year']
        approval_year=schedule_form.cleaned_data['approval_year']
        special=schedule_form.cleaned_data['special']
        college=schedule_form.cleaned_data['college']
        conclude_year = schedule_form.cleaned_data['conclude_year']
        budget_serial_year = schedule_form.cleaned_data['budget_serial_year']
        audite_serial_year = schedule_form.cleaned_data['audite_serial_year']
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
        if conclude_year == "-1":
            conclude_year=''
        if budget_serial_year == "-1":
            budget_serial_year = ''
        if audite_serial_year == "-1":
            audite_serial_year = ''
        q0=(application_status and Q(project_status__status__gte=application_first_status,project_status__status__lte=application_last_status)) or None
        q1=(status and Q(project_status__status__gte=first_status,project_status__status__lte=last_status)) or None
        q2=(application_year and Q(application_year=application_year)) or None
        q3=(approval_year and Q(approval_year=approval_year)) or None
        q4=(special and Q(project_special=special)) or None
        q5=(college and Q(teacher__college=college)) or None
        q7=(conclude_year and Q(conclude_year=conclude_year)) or None
        q8=(budget_serial_year and Q(projectfundbudget__serial_number__startswith = budget_serial_year)) or None
        q9=(audite_serial_year and Q(projectfundsummary__serial_number__startswith = audite_serial_year)) or None
        if other_search:
            sqlstr=other_search
            q6_1=Q(project_code__contains=sqlstr)
            q6_2=Q(project_application_code__contains=sqlstr)
            q6_3=Q(title__contains=sqlstr)
            q6_4=Q(teacher__teacherinfosetting__name__contains=sqlstr)
            q6=reduce(lambda x,y:x|y,[q6_1,q6_2,q6_3,q6_4])
        else:
            q6=None
        qset=filter(lambda x:x!=None,[q0,q1,q2,q3,q4,q5,q6,q7,q8,q9])
        if qset:
            qset=reduce(lambda x,y: x&y ,qset)
            pro_list=get_project_list(request).filter(qset)
        else:
            pro_list=get_project_list(request).all()
        return pro_list

def summaryViewWork(request,pid,is_submited,redirect=False):
    projfundsummary = ProjectFundSummary.objects.get( project_id = pid )
    profundsummaryform = ProFundSummaryForm(instance=projfundsummary)
    profundsummaryremarkmentform = ProFundSummaryRemarkmentForm(instance=projfundsummary)
    project = ProjectSingle.objects.get( project_id = pid)
    context = {
        'projfundsummary':projfundsummary,
        'profundsummaryremarkmentform':profundsummaryremarkmentform,
        'profundsummaryform':profundsummaryform,
        'pid':pid,
        'project':project,
        'redirect':redirect,
        'is_submited':is_submited,
        'showseal':project.project_status.status>=PROJECT_STATUS_FINAL_FINANCE_OVER,
    }
    return context

def finalReportViewWork(request,pid,is_submited,redirect=False):
    final = FinalSubmit.objects.get( project_id = pid)
    loginfo(pid)
    project = ProjectSingle.objects.get( project_id = pid)
    achivement_list = ProjectAchivement.objects.filter( project_id = pid )
    datastatics_list = ProjectStatistics.objects.filter( project_id = pid )
    projfundsummary = ProjectFundSummary.objects.get( project_id = pid )
    projfundbudget = ProjectFundBudget.objects.get( project_id = pid)
    projachivementform  = ProjectAchivementForm()
    projdatastaticsform = ProjectDatastaticsForm()
    profundsummaryform = ProFundSummaryForm(instance=projfundsummary)
    profundsummaryremarkmentform = ProFundSummaryRemarkmentForm(instance=projfundsummary)
    profundbudgetform = ProFundBudgetForm( instance =projfundbudget )
    profundbudgetremarkmentform = ProFundBudgetRemarkmentForm(instance = projfundbudget)
    reports = ProgressReport.objects.filter(project_id = pid).order_by("-year")
    progress_form = ProgressForm()
    if not projfundbudget.finance_staff:
        projfundbudget.finance_staff = u"未填写"
    if not projfundbudget.finance_checktime:
        projfundbudget.finance_checktime = u"未填写"
    if not projfundsummary.finance_staff:
        projfundsummary.finance_staff = u"未填写" 
    if not projfundsummary.finance_checktime:
        projfundsummary.finance_checktime="未填写"

    final_form = FinalReportForm(instance=final)

    page = request.GET.get('page')
    page2 = request.GET.get('page2')
    if page == None:
        page = 1
    if page2 == None:
        page2 = 1
    loginfo(p=redirect, label="redirect")
    context = {
        'projachivementform':projachivementform,
        'projdatastaticsform':projdatastaticsform,
        'final': final_form,
        'pid':pid,
        'redirect':redirect,
        'achivement_list':achivement_list,
        'datastatics_list':datastatics_list,
        'projfundsummary':projfundsummary,
        'profundsummaryform':profundsummaryform,
        'fundbudget_form':profundbudgetform,
        'fundbudgetremarkment_form':profundbudgetremarkmentform,
        'profundsummaryremarkmentform':profundsummaryremarkmentform,
        'is_submited':is_submited,
        'projectbudget':project.project_budget_max,
        'project':project,
        'reports': reports,
        'progress_form': progress_form,
        'pro':project,
        'page':page,
        'page2':page2,
        'fundbudget':projfundbudget,
    }
    return context

def fundBudgetViewWork(request,pid,is_submited,redirect=False):
    fundbudget = ProjectFundBudget.objects.get(project_id = pid)
    project = ProjectSingle.objects.get(project_id = pid)
    # if fundbudget.finance_staff:finance_staff=fundbudget.finance_staff
    # else:finance_staff="未填写"
    # if fundbudget.finance_checktime:finance_checktime=fundbudget.finance_checktime
    # else:finance_checktime="未填写"
    if request.method == "POST":
        fundbudget_form = ProFundBudgetForm(request.POST, instance=fundbudget)
        fundbudgetremarkment_form = ProFundBudgetRemarkmentForm(request.POST,instance=fundbudget)
        if fundbudget_form.is_valid() and fundbudgetremarkment_form.is_valid():
            fundbudgetremarkment_form.save()
            fundbudget_form.save()
            # redirect = True
            status_confirm(request,project)
            loginfo(p=project.project_status,label="status")
        else:
            logger.info("ProFundBudgetForm Valid Failed"+"**"*10)
            logger.info(fundbudget_form.errors)
            logger.info(fundbudgetremarkment_form.errors)
    else:
        fundbudget_form = ProFundBudgetForm(instance=fundbudget)
        fundbudgetremarkment_form=ProFundBudgetRemarkmentForm(instance=fundbudget)
    context = {
        'redirect':redirect,
        'fundbudget_form':fundbudget_form,
        'fundbudgetremarkment_form':fundbudgetremarkment_form,
        'pid':pid,
        'is_submited':is_submited,
        'projectbudget':project.project_budget_max,
        'project':project,
        'fundbudget':fundbudget,
        'showseal':project.project_status.status>=PROJECT_STATUS_TASK_FINANCE_OVER,
    }
    return context

def progressReportViewWork(request, pid, is_submited, redirect = False):
    progress_form = ProgressForm()
    reports = ProgressReport.objects.filter(project_id = pid).order_by("-year")
    context = {
        'redirect': redirect,
        'progress_form': progress_form,
        'pid': pid,
        'is_submited': is_submited,
        'reports': reports,
    }
    return context

def getCollegeListForHtml():
    college_list_choice=[]
    college_list_all = CollegeProfile.objects.all()
    for item in college_list_all:
        college_name = [obj.name for obj in item.college_set.all()]
        cname = ""
        for name in college_name:
            cname=cname+name+'  '
        college_list_choice.append((item.id,item.userid.first_name, cname))
    college_list_choice=list(set(college_list_choice))
    return college_list_choice

from users.models import CollegeProfile
def noticeMessageSettingBase(request,userauth):
    notice_choice=NOTICE_CHOICE
    template_notice_message=TemplateNoticeMessage.objects.all()
    template_notice_message_form = TemplateNoticeMessageForm()
    template_notice_message_group=[]
    cnt=1
    for item in template_notice_message:
        nv={
            "id":item.id,
            "iid":cnt,
            "title":item.title,
            "message":item.message,
        }
        cnt+=1
        template_notice_message_group.append(nv)



    


    notice_form=NoticeForm(request=request)
    context=getContext(template_notice_message_group,1,"item",0)
    context.update({
        "template_notice_message_form":template_notice_message_form,
        "notice_choice":notice_choice,
        "notice_form":notice_form,
        "userauth":userauth,
        # "college_list":college_list_choice,
        
    })
    context.update(getContext(getCollegeListForHtml(), 1, "item2", 0))

    return render(request, userauth['role'] + "/notice_message_setting.html", context)
