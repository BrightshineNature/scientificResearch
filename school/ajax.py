# coding: UTF-8

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template.loader import render_to_string
from django.db.models import Q

from adminStaff.models import ProjectSingle, Re_Project_Expert
from backend.utility import getContext
from users.models import ExpertProfile

@dajaxice_register
def getUnallocProjectPagination(request, page):
    message = ""
    page = int(page)
    project_list = ProjectSingle.objects.all()
    context = getContext(project_list, page, "item", 0)
    html = render_to_string("school/widgets/unalloc_project_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getAllocProjectPagination(request, page):
    message = ""
    page = int(page)
    project_list = ProjectSingle.objects.all()
    context = getContext(project_list, page, "item", 0)
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
    print college_id, special_id
    if college_id == "-1":
        project_list = ProjectSingle.objects.all()
    else:
        project_list = ProjectSingle.objects.filter(teacher__college = college_id)

    if special_id != "-1":
        project_list = project_list.filter(project_special = special_id)

    context = getContext(project_list, 1, "item", 0)

    html_alloc = render_to_string("school/widgets/alloc_project_table.html", context)
    html_unalloc = render_to_string("school/widgets/unalloc_project_table.html", context)
    return simplejson.dumps({"html_alloc": html_alloc, "html_unalloc": html_unalloc, })
