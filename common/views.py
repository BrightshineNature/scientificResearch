# coding: UTF-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from common.forms import  ScheduleBaseForm,ProjectJudgeForm, ProjectMemberForm
from common.utils import get_query_status,get_qset,get_query_application_status
from const import *
from teacher.forms import *
from teacher.models import *
from backend.logging import logger, loginfo
from adminStaff.models import ProjectSingle,TemplateNoticeMessage
from django.db.models import Q
from backend.utility import getContext
from common.forms import ProjectInfoForm, BasisContentForm, BaseConditionForm,NoticeForm
from adminStaff.forms import TemplateNoticeMessageForm
from const.models import ScienceActivityType
from teacher.models import ProjectFundBudget

from common.models import ProjectMember,BasisContent , BaseCondition, UploadFile
def getParam(pro_list, userauth,flag):
    (pending_q,default_q,search_q)=get_qset(userauth)
    not_pass_apply_project_group=pro_list.filter(pending_q)
    if flag:
        pass_apply_project_group=pro_list.filter(default_q)
    else:
        pass_apply_project_group=pro_list.filter(search_q)
    loginfo(pass_apply_project_group.count())
    count=not_pass_apply_project_group.count()+pass_apply_project_group.count()
    param={
        "not_pass_apply_project_group":not_pass_apply_project_group,
        "pass_apply_project_group":pass_apply_project_group,
        "total_count":count,
    }
    return param

def appManage(request, pid):


    

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
        'science_type': p.science_type.category if p.science_type else None,

        'trade_code': p.trade_code,
        'subject_name': p.subject_name,
        'subject_code': p.subject_code,
        'start_time': p.start_time,
        'end_time': p.end_time,
        'project_tpye': p.project_tpye,
    }



    project_member_list = ProjectMember.objects.filter(project__project_id = pid)

    # for i in project_member_list:
    #     i.professional_title_id = i.professional_title.category
    #     i.executive_position_id = i.executive_position.category



    print "UUUUUU***************"



    context = {
        'project_info_form': ProjectInfoForm(project_info_data),
        'project_member_form': ProjectMemberForm(),
        'basis_content_form':basis_content_form,
        'basis_content_id':basis_content_id,

        'base_condition_form':base_condition_form,
        'base_condition_id':base_condition_id,
        'project_member_list': project_member_list,
        'pid': pid,
    }

    return context
    return render(request, userauth['role'] + "/application.html", context)

from django.core.files.storage import default_storage
import time
# def handle_uploaded_file(f):
#     print f.name
#     print f.size
#     # print f.url
#     # print f.path
FileType = [u"基本科研业务费专项项目申请书",
            u"基本科研业务费专项项目进展报告",
            u"基本科研业务费专项项目结题报告",
            u"基本科研业务费专项项目任务书",
            u"其他", ]
def getType(fname):
    for i in FileType:
        if i == fname.split('.')[0]:
            return i
    return FileType[4]

EntranceMapToType= {
    "application_file":u"基本科研业务费专项项目申请书",
    "process_file":u"基本科研业务费专项项目进展报告",
    "final_file":u"基本科研业务费专项项目结题报告",
    "task_file":u"基本科研业务费专项项目任务书",
    "other_file":u"其他",
}
Entrance = [
    "application_file",
    "process_file",
    "final_file",
    "task_file",
    "other_file",
]
AcceptedExtension = [
    'doc', 'docx', 'DOC', 'DOCX',
]
def handleFileUpload(request, pid,  entrance):

    f = request.FILES[entrance]
    print "********CMP::"
    print f.name
    print getType(f.name)
    print entrance
    print EntranceMapToType[entrance]
    ftype = getType(f.name) 
    if(ftype != EntranceMapToType[entrance]):
        return 0
    if ftype != FileType[4]:
        if not AcceptedExtension.count(f.name.split('.')[1]):
            return 0

    obj = UploadFile.objects.filter(project__project_id = pid, name = f.name)
    if obj :
        obj = obj[0] # assert only exist one    
        path = obj.file_obj.path
        obj.delete()
        default_storage.delete(path)
    else :
        pass
    obj = UploadFile()
    obj.name = f.name
    obj.project = ProjectSingle.objects.get(project_id = pid)
    obj.file_obj = f
    obj.upload_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    obj.file_type = ftype
    obj.file_size = f.size
    obj.save()
    return 1


def fileUploadManage(request, pid):

    print "fileUploadManage**********"
    error = 0
    if request.method == 'POST':
        if request.POST.has_key("fid"):
            obj = UploadFile.objects.get(id = request.POST['fid'])
            if obj:
                path = obj.file_obj.path
                obj.delete()
                default_storage.delete(path)






        for i in Entrance:
            if request.FILES.has_key(i):
                if not handleFileUpload(request, pid, i):
                    error = 1
                
            

    else :
        pass
        # form = UploadFileForm()

    files = UploadFile.objects.filter(project__project_id = pid)
    for i in files:
        i.file_size = '%.3f KB' % (float(i.file_size) / 1024)
        # i.file_size += 'KB'

    context = {
        'files': files,
        'error': error
    }
    return context



def scheduleManage(request, userauth):
    loginfo(userauth["role"])
    context = schedule_form_data(request, userauth)
    return render(request, userauth['role'] + '/schedule.html', context)
def researchConcludingManage(request , userauth):
    context = schedule_form_data(request , userauth)
    return render(request, userauth['role']+'/research_concluding.html' ,context)
def financeManage(request, userauth):
    context = schedule_form_data(request, userauth)
    for item in context.get("pass_apply_project_group"):
        item.remain=int(item.projectfundsummary.total_budget)-int(item.projectfundsummary.total_expenditure)
    for item in context.get("not_pass_apply_project_group"):
        item.remain=int(item.projectfundsummary.total_budget)-int(item.projectfundsummary.total_expenditure)
    return render(request, userauth['role'] + '/financeProject.html', context)
def financialManage(request, userauth):
    context = schedule_form_data(request, userauth)

    return render(request, userauth['role'] + '/financial.html', context)
def schedule_form_data(request , userauth=""):

    schedule_form = ScheduleBaseForm()
    ProjectJudge_form=ProjectJudgeForm()
    has_data = False
    if request.method == 'POST':
        schedule_form = ScheduleBaseForm(request.POST)
        pro_list=get_search_data(schedule_form)
        default=False
    else:
        pro_list=ProjectSingle.objects.all()
        default=True
    param=getParam(pro_list,userauth,default)
    context ={ 'schedule_form':schedule_form,
               'has_data': has_data,
               'usercontext': userauth,
               'ProjectJudge_form':ProjectJudge_form,
    }
    context.update(param)

    return context
def get_search_data(schedule_form):
     if schedule_form.is_valid():
            application_status=schedule_form.cleaned_data['application_status']
            status=schedule_form.cleaned_data['status']
            application_year= schedule_form.cleaned_data['application_year']
            approval_year=schedule_form.cleaned_data['approval_year']
            special=schedule_form.cleaned_data['special']
            college=schedule_form.cleaned_data['college']
            conclude_year = schedule_form.cleaned_data['conclude_year']
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
            q0=(application_status and Q(project_status__status__gte=application_first_status,project_status__status__lte=application_last_status)) or None
            q1=(status and Q(project_status__status__gte=first_status,project_status__lte=last_status)) or None
            q2=(application_year and Q(application_year=application_year)) or None
            q3=(approval_year and Q(approval_year=approval_year)) or None
            q4=(special and Q(project_special=special)) or None
            q5=(college and Q(teacher__college=college)) or None
            q7=(conclude_year and Q(conclude_year=conclude_year)) or None
            if other_search:
                sqlstr=other_search
                q6_1=Q(project_code__contains=sqlstr)
                q6_2=Q(project_application_code__contains=sqlstr)
                q6_3=Q(title__contains=sqlstr)
                q6_4=Q(teacher__teacherinfosetting__name__contains=sqlstr)
                q6=reduce(lambda x,y:x|y,[q6_1,q6_2,q6_3,q6_4])
            else:
                q6=None
            qset=filter(lambda x:x!=None,[q0,q1,q2,q3,q4,q5,q6,q7])
            if qset:
                qset=reduce(lambda x,y: x&y ,qset)
                pro_list=ProjectSingle.objects.filter(qset)
            else:
                pro_list=ProjectSingle.objects.all()
            return pro_list


def finalReportViewWork(request,pid,is_submited,redirect=False):
    final = FinalSubmit.objects.get( project_id = pid)
    achivement_list = ProjectAchivement.objects.filter( project_id = pid )
    datastatics_list = ProjectStatistics.objects.filter( project_id = pid )
    projfundsummary = ProjectFundSummary.objects.get( project_id = pid ) 
    projachivementform  = ProjectAchivementForm()
    projdatastaticsform = ProjectDatastaticsForm()
    profundsummaryform = ProFundSummaryForm(instance=projfundsummary)

    # if request.method == "POST":
    #     final_form = FinalReportForm(request.POST, instance=final)
    #     if final_form.is_valid():
    #         final_form.save()
    #         redirect = True
    #     else:
    #         logger.info("Final Form Valid Failed"+"**"*10)
    #         logger.info(final_form.errors)
    # else:
    final_form = FinalReportForm(instance=final)

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
        'is_submited':is_submited,
    }
    return context

def fundBudgetViewWork(request,pid,is_submited,redirect=False):
    fundbudget = ProjectFundBudget.objects.get(project_id = pid)
    print request.method
    if request.method == "POST":
        fundbudget_form = ProFundBudgetForm(request.POST, instance=fundbudget)
        if fundbudget_form.is_valid():
            fundbudget_form.save()
            redirect = True
        else:
            logger.info("ProFundBudgetForm Valid Failed"+"**"*10)
            logger.info(fundbudget_form.errors)
    else:
        fundbudget_form = ProFundBudgetForm(instance=fundbudget)

    context = {
		'redirect':redirect,
		'fundbudget_form':fundbudget_form,
        'pid':pid,
        'is_submited':is_submited,
    }
    return context
    
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
        "userauth":userauth
    })
    return render(request, userauth['role'] + "/notice_message_setting.html", context)
