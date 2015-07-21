# coding: UTF-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template.loader import render_to_string
from django.db.models import Q

from adminStaff.models import Re_Project_Expert
from backend.utility import getContext
from users.models import ExpertProfile
from common.utils import getScoreTable, getScoreForm,getFinalScoreTable,getFinalScoreForm

@dajaxice_register
def getPagination(request, special, college, page, is_first_round):
    message = ""
    expert = ExpertProfile.objects.get(userid = request.user)
    page = int(page)
    re_list = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = is_first_round))
    if special != "-1": 
        re_list = re_list.filter(project__project_special = special)
    if college != "-1":
        re_list = re_list.filter(project__teacher__college = college)

    re_list = list(re_list)
    for re_obj in re_list:
        if is_first_round:
            re_obj.score = getScoreTable(re_obj.project).objects.get_or_create(re_obj = re_obj)[0].get_total_score()
        else:
            re_obj.score = getFinalScoreTable(re_obj.project).objects.get_or_create(re_obj = re_obj)[0].get_total_score()
    re_list.sort(key = lambda x: x.score)
    if is_first_round:
        context = getContext(re_list, page, "item", 0)
        html = render_to_string("expert/widgets/first_round_project_table.html", context)
        message = "first round"
    else:
        context = getContext(re_list, page, "item2", 0)
        html = render_to_string("expert/widgets/second_round_project_table.html", context)
        message = "second round"
    return simplejson.dumps({"message": message, "html": html, })
