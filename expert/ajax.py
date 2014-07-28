# coding: UTF-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template.loader import render_to_string
from django.db.models import Q

from adminStaff.models import Re_Project_Expert
from backend.utility import getContext
from users.models import ExpertProfile

@dajaxice_register
def getPagination(request, page, is_first_round):
    message = ""
    expert = ExpertProfile.objects.get(userid = request.user)
    page = int(page)
    project_list = [re_obj.project for re_obj in Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = is_first_round))]
    if is_first_round:
        context = getContext(project_list, page, "item", 0, 2)
        html = render_to_string("expert/widgets/first_round_project_table.html", context)
        message = "first round"
    else:
        context = getContext(project_list, page, "item2", 0, 2)
        html = render_to_string("expert/widgets/second_round_project_table.html", context)
        message = "second round"
    return simplejson.dumps({"message": message, "html": html, })
