# coding: UTF-8
'''
Created on 2013-3-29

@author: sytmac
'''
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string

#from adminStaff.forms import NumLimitForm, TimeSettingForm, SubjectCategoryForm, ExpertDispatchForm,SchoolDispatchForm,TemplateNoticeForm,FundsChangeForm,StudentNameForm, SchoolDictDispatchForm
from backend.decorators import check_auth
from django.db.models import Q
from backend.logging import loginfo
from django.conf import settings
from django.contrib.auth.models import User
from const import *
from common.utils import status_confirm, statusRollBack

from adminStaff.models import ProjectSingle,Re_Project_Expert
from const.models import ScienceActivityType, NationalTradeCode, Subject
from teacher.models import TeacherInfoSetting,ProjectFundBudget,ProjectFundSummary
from common.models import ProjectMember, BasisContent, BaseCondition
from users.models import AdminStaffProfile,TeacherProfile,ExpertProfile,SchoolProfile,CollegeProfile

from common.views import schedule_form_data,get_search_data
from common.utility import get_xls_path

from common.forms import ProjectInfoForm, ProjectMemberForm,BasisContentForm, BaseConditionForm, ScheduleBaseForm
from django.core.mail import send_mail

OVER_STATUS_NOTOVER = "notover"
OVER_STATUS_OPENCHECK = "opencheck"
OVER_STATUS_MIDCHECK = "midcheck"
OVER_STATUS_FINCHECK = "fincheck"
OVER_STATUS_NORMAL = "normal"

OVER_STATUS_CHOICES = (
    ('no', u"未结题"),
    ('yes', u"已结题"),    
)
from users.models import Special
from common.forms import getSpecialTypeGroup, getTeacherYearGroup

cnt_teacher_list = []

@dajaxice_register
def getSelectedTeacher(request, form):
    form = deserialize_form(form)

    teacher_year_gruop = []
    if form['teacher_year_select'] != u"-1":
        teacher_year_gruop.append(int(form['teacher_year_select']))
    else :
        
        for i in getTeacherYearGroup(request):
            if i[0] == -1: continue
            teacher_year_gruop.append(int(i[0]))

    special_gruop = []
    if form['teacher_special_select'] != u"-1":
        special_gruop.append(Special.objects.get(id = form['teacher_special_select']))
    else:
        for i in getSpecialTypeGroup(request):
            if i[0] == -1: continue
            special_gruop.append(Special.objects.get(id = i[0]))



    project_list = ProjectSingle.objects.filter(approval_year__in = teacher_year_gruop,\
        project_special__in = special_gruop)



    cnt_teacher_list[:] = []
    
    for p in project_list:
        cnt_teacher_list.append((p.teacher.id, p.teacher.userid.first_name, \
                            p.teacher.college, p))

    print "IT IS ME *************^&&&&&&&&&&&&&&&"

    # cnt_teacher_list = teacher_list
    # getContext(getCollegeListForHtml(), 1, "item3", 0)
    # print "TTTTTTTt"
    # print teacher_list
    teacher_table = render_to_string( "widgets/notice_message_setting_select_teacher_table.html",         
        getContext(cnt_teacher_list, 1, "item3", 0),
        )

    print cnt_teacher_list
    return simplejson.dumps({"status":1, "teacher_table":teacher_table})

cnt_expert_list = []
kkk = []
@dajaxice_register
def getSelectedExpert(request, form):

    kkk[:] = []
    form = deserialize_form(form)    
    special_id = form["expert_special_select"]


    special_id_gruop = []
    if special_id != u'-1':
        special_id_gruop.append(special_id);
    else :
        all_special = getSpecialTypeGroup(request)
        for i in all_special:
            if i[0] == -1: continue
            special_id_gruop.append(str(i[0]))

    spe = Special.objects.filter(id__in = special_id_gruop)

    proj_list = ProjectSingle.objects.filter(Q(project_special__in=spe) \
        & Q(project_status__status__gte = PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,\
            project_status__status__lte = PROJECT_STATUS_FINAL_EXPERT_SUBJECT\
            ))


    p_e_group  = Re_Project_Expert.objects.filter(project__in=proj_list).values("expert").distinct()
    p_e_group = ExpertProfile.objects.filter(id__in = [ it['expert'] for it in p_e_group])
    expert_list = []
    for it in p_e_group:
        expert_list.append((it.id, it.userid.first_name, it.college))
    expert_list = list(set(expert_list))
    cnt_expert_list[:] = expert_list



    expert_table = render_to_string( "widgets/notice_message_setting_select_expert_table.html",         
        getContext(expert_list, 1, "item4", 0),
        )
    return simplejson.dumps({"status":1, "expert_table":expert_table})



from common.views import getCollegeListForHtml
from backend.utility import getContext
# @dajaxice_register
# def getCollegeListPagination(request, page):
#     page = int(page)
#     college_list = getCollegeListForHtml()
#     context = getContext(college_list, page, "item2", 0)
#     html = render_to_string("widgets/notice_message_setting_select_college_table.html", context)
#     return simplejson.dumps({"status":1, "html":html,})

@dajaxice_register
def getUserListPagination(request, page, user):
    page = int(page)
    html = ""
    if user == "college":
        user_list = getCollegeListForHtml()
        context = getContext(user_list, page, "item2", 0)
        html = render_to_string("widgets/notice_message_setting_select_college_table.html", context)
    elif user == "teacher":
        user_list = cnt_teacher_list
        context = getContext(user_list, page, "item3", 0)
        html = render_to_string("widgets/notice_message_setting_select_teacher_table.html", context)
    else:
        user_list = cnt_expert_list
        context = getContext(user_list, page, "item4", 0)
        html = render_to_string("widgets/notice_message_setting_select_expert_table.html", context)

    return simplejson.dumps({"status":1, "html":html,})


@dajaxice_register
def SendMail(request,form):
    form=deserialize_form(form)
    print 'SBSBSB****************'
    loginfo(form)
    #send_mail(form["mail_title"],form["mail_content"],"zhc1009@163.com",["347096491@qq.com","369385153@qq.com"])
    if form["mail_title"]=="":
        status=1
    elif form["mail_content"]=="":
        status=2
    else:
        recipient_list=[]

        watch_all_list = []  # for test, watch every one
        if form.get("special"):
            special_group=SchoolProfile.objects.all()
            recipient_list.extend([item.userid.email for item in special_group])
        if form.get("college"):
            # if AdminStaffProfile.objects.filter(userid=request.user).count()>0:
            #     college_group=CollegeProfile.objects.all()
            #     recipient_list.extend([item.userid.email for item in college_group])
            # else:
            college_group=form.getlist("college_list")
            college_group=[int(item) for item in college_group]
            college_group=CollegeProfile.objects.filter(id__in=college_group)
            recipient_list.extend([item.userid.email for item in college_group])
            watch_all_list.extend([item.userid.first_name for item in college_group])
        if form.get("teacher"):
            teacher_group=form.getlist("teacher_list")
            teacher_group=[int(item) for item in teacher_group]
            teacher_group=TeacherProfile.objects.filter(id__in=teacher_group)
            recipient_list.extend([item.userid.email for item in teacher_group])
            watch_all_list.extend([item.userid.first_name for item in teacher_group])
            # if AdminStaffProfile.objects.filter(userid=request.user).count()>0:
            #     teacher_group=TeacherProfile.objects.all()
            #     recipient_list.extend([item.userid.email for item in teacher_group])
            # else:
            #     year_group=form.getlist("teacher_year")
            #     sp_group=form.getlist("teacher_special")
            #     sp_group=[int(item) for item in sp_group]
            #     project_group=ProjectSingle.objects.filter(application_year__in=year_group,project_special__in=sp_group)
            #     teacher_group=[item.teacher for item in project_group]
            #     recipient_list.extend([item.userid.email for item in teacher_group])
        if form.get("expert"):
            expert_group=form.getlist("expert_list")
            expert_group=[int(item) for item in expert_group] 
            expert_group=ExpertProfile.objects.filter(id__in=expert_group)
            recipient_list.extend([item.userid.email for item in expert_group])

            watch_all_list.extend([item.userid.first_name for item in expert_group])
            # if AdminStaffProfile.objects.filter(userid=request.user).count()>0:
            #     expert_group=ExpertProfile.objects.all()
            #     recipient_list.extend([item.userid.email for item in expert_group])
            # else:
            #     year_group=form.getlist("expert_year")
            #     sp_group=form.getlist("expert_special")
            #     sp_group=[int(item) for item in sp_group]
            #     project_group=ProjectSingle.objects.filter(application_year__in=year_group,project_special__in=sp_group)
            #     expert_group=[]
            #     for project in project_group:
            #         p_e_group=Re_Project_Expert.objects.filter(project=project)
            #         expert_group.extend([item.expert for item in p_e_group])
            #     expert_group=list(set(expert_group))
            #     recipient_list.extend([item.userid.email for item in expert_group])
        print "#################&&&&&&&&&&&&&&&&&&&&&&&&&&&7"
        loginfo( recipient_list)
        for i in watch_all_list:
            print i
        print "#################"
        if len(recipient_list)==0:
            status=3
        else:
            status=0
            title = form["mail_title"]
            # render_to_string('email/email_2_expert_title.txt',
            #                          {"email_title":form["mail_title"]})
            content = form["mail_content"]
            # render_to_string('email/email_2_expert_content.txt',
            #                           {"email_content":form["mail_content"]})

            

            send_mail(title,content,settings.DEFAULT_FROM_EMAIL,recipient_list)
    return simplejson.dumps({"status":status})

@dajaxice_register
def getStatus(request):
    return simplejson.dumps({
        "application_c":PROJECT_STATUS_APPLICATION_COMMIT_OVER,
        "application_s":PROJECT_STATUS_APPLICATION_COLLEGE_OVER,
        "final":PROJECT_STATUS_FINAL_FINANCE_OVER,
    })
@dajaxice_register
def LookThroughResult(request,judgeid,userrole,userstatus,page,page2,search,look_through_form,searchForm):
    project=ProjectSingle.objects.get(pk=judgeid)
    form=deserialize_form(look_through_form)
    if form["judgeresult"]=="1":
        project.comment=''
        project.save()
        if userstatus=="application" and userrole=="school" and not project.project_special.review_status:
            set_status(project,PROJECT_STATUS_APPROVAL)
        else:
            status_confirm(project,-1)
        if userstatus=="application":
            if form.get("max_budget"):
                project.project_budget_max=int(form.get("max_budget"))
                project.save()
                loginfo(project.project_budget_max)
        if userstatus=="budget":
            finance_budget=ProjectFundBudget.objects.get(project_id=project)
            finance_budget.comment=form.get("reason")
            finance_budget.save()
        if userstatus=="final":
            finance_summary=ProjectFundSummary.objects.get(project_id=project)
            finance_summary.finance_comment=form.get("reason")
            finance_summary.save()
    else:
        print form.getlist('application')
        identity = request.session.get("auth_role","")
        if identity == SCHOOL_USER:
            school = SchoolProfile.objects.get(userid = request.user)
            comment= school.department+u"管理员"+school.userid.first_name+u":"
        elif identity == COLLEGE_USER:
            comment= u"学院管理员"+request.user.first_name+u":"
        elif identity == FINANCE_USER:
            comment= u"财务管理员"+request.user.first_name+u":"
        else:
            comment = u""
        for item in form.getlist('application'):
            comment+=item+u""
        for item in form.getlist("final"):
            comment+=item+u"、"
        comment+=u",原因"+form["reason"]
        loginfo(comment)
        project.comment=comment
        project.save()
        statusRollBack(project,userrole,userstatus,form)
    context=schedule_form_data(request,{
        "role":userrole,
        "status":userstatus
    },searchForm,page,page2,search)
    loginfo(userstatus)
    if userstatus=="application":
        table_html=render_to_string("widgets/project_info.html",context)
    else:
        table_html=render_to_string("widgets/research_concluding_table.html",context)
    return simplejson.dumps({"table_html":table_html}) 
from common.utils import set_status
@dajaxice_register
def StatusChange(request,judgeid,status,page2,searchForm):
    project=ProjectSingle.objects.get(pk=judgeid)
    set_status(project,int(status))
    project.save()
    loginfo(status)
    return getPagination(request,-1,page2,"adminStaff","researchConcluding",0,searchForm)

@dajaxice_register
def getPagination(request,page,page2,userrole,userstatus,search,form):
    userauth={
        "role":userrole,
        "status":userstatus
    }
    page=int(page)
    page2=int(page2)
    search=int(search)
    loginfo(userrole)
    loginfo(form)
    loginfo(userstatus)
    context=schedule_form_data(request,userauth,form,page,page2,search)
    if userstatus=="application":
        table_not_pass=render_to_string("widgets/project_info_not_pass_table.html",context)
        table_pass=render_to_string("widgets/project_info_pass_table.html",context)
    else:
        table_not_pass=render_to_string("widgets/research_concluding_table_not_pass.html",context)
        table_pass=render_to_string("widgets/research_concluding_table_pass.html",context)
    return simplejson.dumps({
            "table_not_pass":table_not_pass,
            "table_pass":table_pass
        })
# @dajaxice_register
# def change_project_overstatus(request, project_id, changed_overstatus):
#     '''
#     change project overstatus
#     '''
#     choices = dict(OVER_STATUS_CHOICES)


#     res = choices[changed_overstatus]    
#     return simplejson.dumps({'status':'1', 'res':res})

#     if changed_overstatus in choices:
#         AdminStaffService.ProjectOverStatusChange(project_id, changed_overstatus)
#         res = choices[changed_overstatus]
#     else:
#         res = "操作失败，请重试"
#     return simplejson.dumps({'status':'1', 'res':res})



@dajaxice_register
def saveProjectInfoForm(request, form, pid):
    form = ProjectInfoForm(deserialize_form(form))


    p = ProjectSingle.objects.get(project_id = pid)
    context = {
        'status': 1,
        'error': None,
    }
    if form.is_valid():        
        p.title = form.cleaned_data['project_name']        

        science_type =form.cleaned_data['science_type']
        p.science_type = ScienceActivityType.objects.get(category=science_type)

        trade_code = form.cleaned_data['trade_code']
        p.trade_code = NationalTradeCode.objects.get(category = trade_code)

        subject = form.cleaned_data['subject']
        p.subject = Subject.objects.get(category = subject)
        
        p.start_time = form.cleaned_data['start_time']
        p.end_time = form.cleaned_data['end_time']
        p.project_tpye = None

        if p.start_time > p.end_time:
            context['status'] = 2
            context['error'] = None            
        else :
            p.save()
    else :
        print "error in saveProjectInfoForm"
        
        error = ""
        for i in form.errors:
            error += i + ","
        print form.errors
        context['status'] = 0
        context['error'] = error
    # print context['error']
    
    return simplejson.dumps(context)


def refreshMemberTabel(pid):
    project_member_list = ProjectMember.objects.filter(project__project_id = pid)

    return render_to_string( "widgets/project_member_table.html", {
        'project_member_list':project_member_list,
        'is_submited':True, 

        })


def checkCanAddMember(request,icard):
    if check_auth(request.user,TEACHER_USER):
        if TeacherProfile.objects.get(userid=request.user).teacherinfosetting.card == icard:
            return False
    try:
        teacherInfo =TeacherInfoSetting.objects.get(card=icard)
        pro = ProjectSingle.objects.filter(Q(teacher=teacherInfo.teacher) & Q(project_status__status__lt =PROJECT_STATUS_OVER))
    except:
        pro = ProjectSingle.objects.none()
    member = ProjectMember.objects.filter(card = icard)
    if member.count() + pro.count()  < 3:
        return True
    else:
        return False


@dajaxice_register
def saveProjectMember(request, form, pid, mid): 
    # save member info into the  member that mid is "mid"
    card_id =""
    if mid:   # modify
        mem = ProjectMember.objects.get(id = mid)
        card_id =mem.card
        form = ProjectMemberForm(deserialize_form(form),instance = mem)
    else :     # save
        form = ProjectMemberForm(deserialize_form(form))
    context = {
        'status':0,
        'error': "",
        'project_member_table': "",
    }

    if form.is_valid(): 
        ok=True
        if not mid:
            ok = checkCanAddMember(request,form.cleaned_data["card"])
        elif mem.card != card_id:
            ok = checkCanAddMember(request,mem.card)
        if ok: 

            temp = form.save(commit = False)
            temp.project = ProjectSingle.objects.get(project_id = pid)
            temp.save()
            context['status'] = 1
            context['project_member_table'] = refreshMemberTabel(pid)
        else :
            context['status'] = 2
            context['error'] = "<h3>此成员被添加次数超过规定限制,不可添加到本项目中</h3>"

    else:
        context['status'] = 3
        error = ""
        for i in form.errors: error += i + ","
        context['error'] = error


    return simplejson.dumps(context)
@dajaxice_register
def deleteProjectMember(request, mid, pid):
    ProjectMember.objects.get(id = mid).delete()

    context = {
        'status':1,
        'project_member_table':refreshMemberTabel(pid),
    }
    return simplejson.dumps(context)

@dajaxice_register
def saveBasisContent(request, form, pid, bid):


    context = {
        'status':1,
    }
    if bid :
        basis_content = BasisContent.objects.get(id = bid)
        form = BasisContentForm(deserialize_form(form), instance = basis_content)
    else :
        form = BasisContentForm(deserialize_form(form))

    if form.is_valid():
        print "OK"
        temp = form.save(commit = False)
        temp.project = ProjectSingle.objects.get(project_id = pid)
        temp.save()
    else:
        print form.errors
        print "error in saveBasisContent"
        context['status'] = 0
    
    return simplejson.dumps(context)

@dajaxice_register
def saveBaseCondition(request, form, pid, bid):

    if bid :
        base_condition = BaseCondition.objects.get(id = bid)
        form = BaseConditionForm(deserialize_form(form), instance = base_condition)
    else :
        form = BaseConditionForm(deserialize_form(form))

    context = {
        'status':1,
    }
    if form.is_valid():
        print "OK"
        temp = form.save(commit = False)
        temp.project = ProjectSingle.objects.get(project_id = pid)
        temp.save()
    else:
        context['status'] = 0
        print form.errors
        print "error in saveBaseCondition"
    
    return simplejson.dumps(context)

from common.utils import status_confirm
@dajaxice_register
def checkValid(request, pid):

    project = ProjectSingle.objects.get(project_id = pid)
    context = {
        'status': 1,
        'error':"",
    }
    error = ""
    if not project.title :
        context['status'] = 0
        error += u"您的‘项目信息‘页面下有未填写字段"

        # print '0'
    elif not project.science_type :
        context['status'] = 0
        error += u"您的‘项目信息‘页面下有未填写字段"
        # print '1'
    elif not project.trade_code :
        context['status'] = 0
        error += u"您的‘项目信息‘页面下有未填写字段"
        # print '2'
    elif not project.subject :
        context['status'] = 0
        error += u"您的‘项目信息‘页面下有未填写字段"
        # print '3'
    elif not project.start_time :
        context['status'] = 0
        error += u"您的‘项目信息‘页面下有未填写字段"
        # print '5'
    elif not project.end_time :
        context['status'] = 0
        error += u"您的‘项目信息‘页面下有未填写字段"


    basis_content = BasisContent.objects.get(project__project_id = pid)
    if not basis_content.basis:
        print "SBSB ^^^^"
        context['status'] = 0
        error = u"您的‘ 立项依据与研究内容‘页面下有未填写字段"

    
    if context['status']:
        loginfo("mdoify success")
        status_confirm(project, APPLICATION_WEB_CONFIRM)

    context['error'] = error
    return simplejson.dumps(context)
@dajaxice_register
def ExportExcel(request,form,category):
    schedule_form = ScheduleBaseForm(deserialize_form(form))
    pro_list=get_search_data(request,schedule_form)
    path = get_xls_path(request,category,pro_list)
    return simplejson.dumps({"status": "ok","path":path})

@dajaxice_register
def ExportTeacherInfoExcel(request,category):
    path = get_xls_path(request,category,"")
    return simplejson.dumps({"status": "ok","path":path})
