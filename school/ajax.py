# coding: UTF-8

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template.loader import render_to_string
from django.db.models import Q
from dajaxice.utils import deserialize_form
from backend.logging import loginfo
from common.utils import status_confirm
from common.utility import get_xls_path
from adminStaff.utility import getSpecial
from adminStaff.models import ProjectSingle, Re_Project_Expert
from backend.utility import getContext
from users.models import ExpertProfile
from const import *
from common.utils import status_confirm, getScoreTable, getScoreForm
from const.models import ProjectStatus
from school.forms import ExpertReviewForm
from common.views import get_project_list

@dajaxice_register
def getUnallocProjectPagination(request, page, college_id, special_id, path):
    message = ""
    page = int(page)
    if path == FIRST_ROUND_PATH:
        project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    else:
        project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_SCHOOL_OVER)

    if college_id != "-1":
        project_list = project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        project_list = project_list.filter(project_special = special_id)

    context = getContext(project_list, page, "item", 0)
    html = render_to_string("school/widgets/unalloc_project_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getAllocProjectPagination(request, page, college_id, special_id, path):
    message = ""
    page = int(page)
    if path == FIRST_ROUND_PATH:
        project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    else:
        project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT)

    if college_id != "-1":
        project_list = project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        project_list = project_list.filter(project_special = special_id)

    context = getContext(project_list, page, "item2", 0)
    html = render_to_string("school/widgets/alloc_project_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getAllocExpertPagination(request, id, page, path):
    message = ""
    page = int(page)
    is_first_round = (path == FIRST_ROUND_PATH)

    if id == "-1": expert_list = ExpertProfile.objects.all()
    else: expert_list = ExpertProfile.objects.filter(college__id = id)
    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = is_first_round)).count()

    context = getContext(expert_list, page, "item3", 0)
    html = render_to_string("school/widgets/alloc_expert_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getExpertList(request, id, path):
    message = ""
    is_first_round = (path == FIRST_ROUND_PATH)
    if id == '-1': expert_list = ExpertProfile.objects.all()
    else: expert_list = ExpertProfile.objects.filter(college__id = id)
    for expert in expert_list:
        expert.alloc_num = Re_Project_Expert.objects.filter(Q(expert = expert) & Q(is_first_round = is_first_round)).count()
    context = getContext(expert_list, 1, "item3", 0)
    html = render_to_string("school/widgets/alloc_expert_table.html", context)
    return simplejson.dumps({"message": message, "html": html, })

@dajaxice_register
def getProjectList(request, college_id, special_id, path):
    if path == FIRST_ROUND_PATH:
        alloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
    else:
        alloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT)

    if college_id != "-1":
        alloc_project_list = alloc_project_list.filter(teacher__college = college_id)
    if special_id != "-1":
        alloc_project_list = alloc_project_list.filter(project_special = special_id)
    if path == FIRST_ROUND_PATH:
        unalloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
    else:
        unalloc_project_list = get_project_list(request).filter(project_status__status = PROJECT_STATUS_FINAL_SCHOOL_OVER)
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
def allocProjectToExpert(request, project_list, expert_list, path):
    message = ""
    is_first_round = (path == FIRST_ROUND_PATH)

    if len(project_list) == 0 or len(expert_list) == 0:
        message = "no project" if len(project_list) == 0 else "no expert"
    else:
        expert_list = [ExpertProfile.objects.get(userid__username = user) for user in expert_list]
        for project_id in project_list:
            project = ProjectSingle.objects.get(project_id = project_id)
            for expert in expert_list:
                try:
                    re_obj = Re_Project_Expert.objects.get(project = project, expert = expert, is_first_round = is_first_round)
                    re_obj.delete()
                except:
                    pass
                finally:
                    re_obj = Re_Project_Expert(project = project, expert = expert, is_first_round = is_first_round)
                    re_obj.save()
                    table = getScoreTable(project)
                    table(re_obj = re_obj).save()
            if path == FIRST_ROUND_PATH:
                project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
            else:
                project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT)
            project.save()
        message = "ok"
    return simplejson.dumps({"message": message, })

@dajaxice_register
def cancelProjectAlloc(request, project_list, path):
    message = ""
    is_first_round = (path == FIRST_ROUND_PATH)

    if len(project_list) == 0:
        message = "no project"
    else:
        for project_id in project_list:
            project = ProjectSingle.objects.get(project_id = project_id)
            for re_obj in Re_Project_Expert.objects.filter(Q(project = project) & Q(is_first_round = is_first_round)):
                re_obj.delete()
            if path == FIRST_ROUND_PATH:
                project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_APPLICATION_SCHOOL_OVER)
            else:
                project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_FINAL_SCHOOL_OVER)
            project.save()
        message = "ok"
    return simplejson.dumps({"message": message,})


@dajaxice_register
def queryAllocedExpert(request, project_id, path):
    message = ""
    is_first_round = (path == FIRST_ROUND_PATH)
    project = ProjectSingle.objects.get(project_id = project_id)
    expert_list = [re_obj.expert for re_obj in Re_Project_Expert.objects.filter(Q(project = project) & Q(is_first_round = is_first_round))]

    html = ''
    for expert in expert_list:
        html += r'<p>' + expert.__str__() + r'</p>'

    return simplejson.dumps({"html": html, })

@dajaxice_register
def ChangeExpertReview(request,form,special_id):
    special = getSpecial(request).get(id = special_id)
    if special:
        expert_form = ExpertReviewForm(deserialize_form(form),instance=special)
        if expert_form.is_valid():
            prolist = ProjectSingle.objects.filter(project_special=special)
            if prolist.count()==0:
                expert_form.save()
                loginfo("success")
                return simplejson.dumps({'status':'1'})
            else:
                return simplejson.dumps({'status':'2'})
    return simplejson.dumps({'status':'0'})
@dajaxice_register
def ChangeControlStatus(request,special_id,type_id,type_name):
    special = getSpecial(request).get(id = special_id)
    if special:
        type=(type_id,type_name)
        if type in CONTROL_TYPE_CHOICES:
            bValue = not getattr(special,type_id+"_status")
            if type_id == TYPE_ALLOC[0]:
                if bValue:
                    pro_list = ProjectSingle.objects.filter(Q(project_special=special) and Q(project_status__status = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT))
                    loginfo(pro_list)
                    for pro in pro_list:
                        status_confirm(pro,APPLICATION_REVIEW_START_CONFIRM)
                else:
                    pro_list = ProjectSingle.objects.filter(Q(project_special=special) and Q(project_status__status = PROJECT_STATUS_APPLICATION_REVIEW_START))
                    loginfo(pro_list)
                    for pro in pro_list:
                        status_confirm(pro,APPLICATION_REVIEW_CONFIRM)
            elif type_id == TYPE_FINAL_ALLOC[0]:
                if bValue:
                   pro_list = ProjectSingle.objects.filter(Q(project_special=special) and Q(project_status__status = PROJECT_STATUS_FINAL_EXPERT_SUBJECT))
                   loginfo(pro_list)
                   for pro in pro_list:
                       status_confirm(pro,FINAL_REVIEW_START_CONFIRM)
                else:
                    pro_list = ProjectSingle.objects.filter(Q(project_special=special) and Q(project_status__status = PROJECT_STATUS_FINAL_REVIEW_START))
                    loginfo(pro_list)
                    for pro in pro_list:
                        status_confirm(pro,FINAL_REVIEW_CONFIRM)
            elif type_id == TYPE_APPLICATION[0]:
                pass
            elif type_id == TYPE_TASK[0]:
                pass
            elif type_id == TYPE_PROGRESS[0]:
                pass
            elif type_id == TYPE_FINAL[0]:
                pass
            setattr(special,type_id+"_status",bValue)
            special.save()
        return simplejson.dumps({'status':'1','type_id':type_id,'type_name':type_name,'value':bValue})
    return simplejson.dumps({'status':'0'})

@dajaxice_register
def getScore(request, pid):
    message = ""
    project = ProjectSingle.objects.get(project_id = pid)
    is_first_round = True
    if project.project_status.status == PROJECT_STATUS_FINAL_REVIEW_OVER:
        is_first_round = False

    scoreTableType = getScoreTable(project)
    scoreFormType = getScoreForm(project)
    scoreList = []
    ave_score = {}
    for re_obj in Re_Project_Expert.objects.filter(Q(project = project) & Q(is_first_round = is_first_round)):
        table = scoreTableType.objects.get(re_obj = re_obj)
        score_row = scoreFormType(instance = table)

        for i, field in enumerate(score_row):
            ave_score[i] = ave_score.get(i, 0) + int(field.value())

        score_row.expert_name = re_obj.expert
        score_row.total_score = table.get_total_score()

        ave_score["total"] = ave_score.get("total", 0) + score_row.total_score

        scoreList.append(score_row)
    if len(scoreList):
        for item in ave_score.items():
            ave_score[item[0]] = 1.0 * item[1] / len(scoreList)
    html = render_to_string("widgets/concluding_data.html", {"scoreList": scoreList, "ave_score": ave_score.values(), "form": scoreFormType,})
    return simplejson.dumps({"message": message, "html": html,})
@dajaxice_register
def ExpertinfoExport(request,special_id,eid):
    special = getSpecial(request).get(id = special_id)
    if special:
        if eid==TYPE_ALLOC[0]:
            proj_set = ProjectSingle.objects.filter(Q(project_special=special) and Q(project_status__status__gte = PROJECT_STATUS_APPLICATION_REVIEW_OVER,project_status__status__lte = PROJECT_STATUS_APPROVAL))
        elif eid == TYPE_FINAL_ALLOC[0]:
            proj_set = ProjectSingle.objects.filter(Q(project_special=special) and Q(project_status__status__gte = PROJECT_STATUS_FINAL_REVIEW_OVER,project_status__status__lte = PROJECT_STATUS_OVER))
        loginfo(proj_set.count())
        path = get_xls_path(request,special.expert_review.category,proj_set,special.expert_review.category)
        ret = {'path':path}
        return simplejson.dumps(ret)
    return simplejson.dumps({'status':'0'})
