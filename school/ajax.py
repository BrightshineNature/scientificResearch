# coding: UTF-8

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template.loader import render_to_string

from adminStaff.models import ProjectSingle
from backend.utility import getContext

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
    print page
    project_list = ProjectSingle.objects.all()
    context = getContext(project_list, page, "item", 0)
    html = render_to_string("school/widgets/alloc_project_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

