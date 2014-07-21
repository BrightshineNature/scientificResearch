# coding: UTF-8
from adminStaff.models import ProjectSingle
from backend.logging import loginfo
from django.db.models import Q
from const import *

def get_application_year_choice():
    project_group=ProjectSingle.objects.all()
    year = [('-1',u"申请年度")]
    year_has=[]
    for item in project_group:
        year_has.append(item.application_year)
    year_has=list(set(year_has))
    
    for y in year_has:
        year.append((y,y))
    return tuple(year)
def get_approval_year_choice():
    project_group=ProjectSingle.objects.all()
    year = [('-1',u"立项年度")]
    year_has=[]
    for item in project_group:
        year_has.append(item.approval_year)
    year_has=list(set(year_has))
    for y in year_has:
        year.append((y,y))
    return tuple(year)
def get_status_choice():
    status_choice=[
        (PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,u"申请书阶段"),
        (PROJECT_STATUS_TASK_OVER,u"任务书阶段"),
        (PROJECT_STATUS_PROGRESS_SCHOOL_OVER,u"进展报告阶段"),
        (PROJECT_STATUS_FINAL_EXPERT_SUBJECT,u"结题书阶段"),
        (PROJECT_STATUS_OVER,u"结题")
    ]
    return status_choice
def get_application_status_choice():
    application_status_choice=[
        (PROJECT_STATUS_APPLICATION_COMMIT_OVER,u"待审核"),
        (PROJECT_STATUS_APPLICATION_COLLEGE_OVER,u"院级审核完成"),
        (PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,u"专题审核完成"),
    ]
    return application_status_choice
def get_query_status(status):
    status=int(status)
    if status==PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT:
        return (0,PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    elif status==PROJECT_STATUS_TASK_OVER:
        return (PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT+1,status)
    elif status==PROJECT_STATUS_PROGRESS_SCHOOL_OVER:
        return (PROJECT_STATUS_TASK_OVER+1,status)
    elif status==PROJECT_STATUS_FINAL_EXPERT_SUBJECT:
        return (PROJECT_STATUS_PROGRESS_SCHOOL_OVER+1,status)
    else:
        return (status,status)
def get_query_application_status(status):
    status=int(status)
    if status==PROJECT_STATUS_APPLICATION_COMMIT_OVER:
        return (0,status)
    elif status==PROJECT_STATUS_APPLICATION_COLLEGE_OVER:
        return (status,status)
    else:
        return (PROJECT_STATUS_APPLICATION_SCHOOL_OVER,status)

def create_QE(status):
    return Q(project_status__status=status)
def create_Q(start,end):

    return Q(project_status__status__gte=start,project_status__status__lte=end)

def get_qset(userauth):
    if userauth['role']=="school" :
        if userauth['status']=="application":
            pending=create_QE(PROJECT_STATUS_APPLICATION_COLLEGE_OVER)
            default=create_QE(PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
            search=create_Q(PROJECT_STATUS_APPLY,PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
        else:
            pending=create_QE(PROJECT_STATUS_TASK_COMMIT_OVER)|create_QE(PROJECT_STATUS_PROGRESS_COMMIT_OVER)|create_QE(PROJECT_STATUS_FINAL_COMMIT_OVER)
            default=create_QE(PROJECT_STATUS_TASK_SCHOOL_OVER)|create_QE(PROJECT_STATUS_PROGRESS_SCHOOL_OVER)|create_QE(PROJECT_STATUS_FINAL_SCHOOL_OVER)
            search=create_Q(PROJECT_STATUS_APPROVAL,PROJECT_STATUS_OVER)
    else:
        if userauth['status']=="application":
            pending=create_QE(PROJECT_STATUS_APPLICATION_COMMIT_OVER)
            default=create_QE(PROJECT_STATUS_APPLICATION_COLLEGE_OVER)
            search=create_Q(PROJECT_STATUS_APPLY,PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
        else:
            pending=Q()
            default=create_QE(PROJECT_STATUS_TASK_SCHOOL_OVER)|create_QE(PROJECT_STATUS_PROGRESS_SCHOOL_OVER)|create_QE(PROJECT_STATUS_FINAL_SCHOOL_OVER)
            search=create_Q(PROJECT_STATUS_APPROVAL,PROJECT_STATUS_OVER)
    return (pending,default,search)
