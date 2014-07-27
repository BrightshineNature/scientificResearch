# coding: UTF-8

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template.loader import render_to_string
from django.db.models import Q

from adminStaff.models import ProjectSingle, Re_Project_Expert
from backend.utility import getContext
from users.models import ExpertProfile
from const import *
from common.utils import status_confirm
from const.models import ProjectStatus

@dajaxice_register
def getUnallocProjectPagination(request, page, college_id, special_id):
    message = ""
    page = int(page)
    project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    if college_id != "-1":
        project_list = project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        project_list = project_list.filter(project_special = special_id)

    context = getContext(project_list, page, "item", 0)
    html = render_to_string("school/widgets/unalloc_project_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getAllocProjectPagination(request, page, college_id, special_id):
    message = ""
    page = int(page)

    print page, college_id, special_id
    project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    if college_id != "-1":
        project_list = project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        project_list = project_list.filter(project_special = special_id)

    context = getContext(project_list, page, "item2", 0)
    html = render_to_string("school/widgets/alloc_project_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getAllocExpertPagination(request, id, page):
    message = ""
    page = int(page)
    if id == "-1": expert_list = ExpertProfile.objects.all()
    else: expert_list = ExpertProfile.objects.filter(college__id = id)
    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True)).count()

    context = getContext(expert_list, page, "item3", 0)
    html = render_to_string("school/widgets/alloc_expert_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getExpertList(request, id):
    message = ""
    if id == '-1': expert_list = ExpertProfile.objects.all()
    else: expert_list = ExpertProfile.objects.filter(college__id = id)
    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = True)).count()
    context = getContext(expert_list, 1, "item3", 0)
    html = render_to_string("school/widgets/alloc_expert_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getProjectList(request, college_id, special_id):
    alloc_project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    if college_id != "-1":
        alloc_project_list = alloc_project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        alloc_project_list = alloc_project_list.filter(project_special = special_id)
    
    unalloc_project_list = ProjectSingle.objects.filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    if college_id != "-1":
        unalloc_project_list = unalloc_project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        unalloc_project_list = unalloc_project_list.filter(project_special = special_id)
    

    context = getContext(unalloc_project_list, 1, "item", 0)
    context2 = getContext(alloc_project_list, 1, "item2", 0)
    
    html_alloc = render_to_string("school/widgets/alloc_project_table.html", context2)
    html_unalloc = render_to_string("school/widgets/unalloc_project_table.html", context)
    return simplejson.dumps({"html_alloc": html_alloc, "html_unalloc": html_unalloc, })

@dajaxice_register
def allocProjectToExpert(request, project_list, expert_list):
    message = ""
    if len(project_list) == 0 or len(expert_list) == 0:
        message = "no project" if len(project_list) == 0 else "no expert"
    else:
        expert_list = [ExpertProfile.objects.get(userid__username = user) for user in expert_list]
        for project_id in project_list:
            project = ProjectSingle.objects.get(project_id = project_id)
            for expert in expert_list:
                try:
                    re_obj = Re_Project_Expert.objects.get(project = project, expert = expert, is_first_round = True)
                    re_obj.delete()
                except:
                    pass
                finally:
                    Re_Project_Expert(project = project, expert = expert, is_first_round = True).save()
            
            project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
            project.save()
        message = "ok"
    
    return simplejson.dumps({"message": message, })

@dajaxice_register
def cancelProjectAlloc(request, project_list):
    message = ""
    if len(project_list) == 0:
        message = "no project"
    else:
        for project_id in project_list:
            project = ProjectSingle.objects.get(project_id = project_id)
            for re_obj in Re_Project_Expert.objects.filter(Q(project = project) & Q(is_first_round = True)):
                re_obj.delete()
        project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
        project.save()
        message = "ok"
    return simplejson.dumps({"message": message,})


@dajaxice_register
def queryAllocedExpert(request, project_id):
    message = ""
    project = ProjectSingle.objects.get(project_id = project_id)
    expert_list = [re_obj.expert for re_obj in Re_Project_Expert.objects.filter(Q(project = project) & Q(is_first_round = True))]

    html = ''
    for expert in expert_list:
        html += r'<p>' + expert.__str__() + r'</p>'

    return simplejson.dumps({"html": html, })
