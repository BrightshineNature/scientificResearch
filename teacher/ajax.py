# coding: UTF-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form

from django.http import Http404
from django.utils import simplejson
from teacher.forms import *
from teacher.models import *
from const.models import *
from const import FINAL_WEB_CONFIRM 
from common.utils import  status_confirm
from backend.logging import logger, loginfo
from django.template.loader import render_to_string
@dajaxice_register
def achivementChange(request,form,achivementid,pid,is_submited):

    achivementform = ProjectAchivementForm(deserialize_form(form))
    projectsingle = ProjectSingle.objects.get(project_id=pid)
    finalsubmit = FinalSubmit.objects.get(project_id = projectsingle)
    message=""
    if achivementform.is_valid():
        achivementtitle = achivementform.cleaned_data["achivementtitle"]
        mainmember = achivementform.cleaned_data["mainmember"]
        introduction = achivementform.cleaned_data["introduction"]
        remarks = achivementform.cleaned_data["remarks"]
        achivementtype = achivementform.cleaned_data["achivementtype"]
        achivementtype=AchivementTypeDict.objects.get(achivementtype=achivementtype)
        if achivementid == 0:
            new_achivement = ProjectAchivement(achivementtitle=achivementtitle,mainmember=achivementtitle,introduction=introduction,remarks=remarks,
                achivementtype=achivementtype,project_id=projectsingle)
            new_achivement.save()
            message = u"新的研究成果添加成功"
            loginfo(p=achivementtitle,label="achivementtitle")
        else:
            old_achivement = ProjectAchivement.objects.get(content_id=achivementid)
            old_achivement.achivementtitle = achivementtitle
            old_achivement.mainmember = mainmember
            old_achivement.introduction = introduction
            old_achivement.remarks = remarks
            old_achivement.achivementtype = achivementtype
            old_achivement.save()
            message = u"修改成功"
    else:
        logger.info("achivementform Valid Failed"+"**"*10)
        logger.info(achivementform.errors)
        message = u"数据没有填完整，请重新填写"
    table = refresh_achivement_table(request,pid,is_submited) 
    ret={'table':table,'message':message,}
    return simplejson.dumps(ret)


def refresh_achivement_table(request,pid,is_submited):
    achivement_list = ProjectAchivement.objects.filter(project_id = pid)
    return render_to_string("widgets/finalreport/final_achivement_table.html",
                            {        
                                'pid':pid,
                                'achivement_list':achivement_list,
                                'is_submited':is_submited,
        })

@dajaxice_register
def achivementDelete(request,achivementid,pid,is_submited):
    projectsingle = ProjectSingle.objects.get(project_id=pid)
    delete_achivement = ProjectAchivement.objects.get(content_id = achivementid)
    delete_achivement.delete()
    table = refresh_achivement_table(request,pid,is_submited) 
    ret = {'message':u'删除成功','table':table}
    return simplejson.dumps(ret)

@dajaxice_register
def datastaticsChange(request,form,datastaticsid,pid,is_submited):

    datastaticsform = ProjectDatastaticsForm(deserialize_form(form))
    projectsingle = ProjectSingle.objects.get(project_id = pid)
    finalsubmit = FinalSubmit.objects.get(project_id=projectsingle)
    message=""
    if datastaticsform.is_valid():
        statics_num = datastaticsform.cleaned_data["statics_num"]
        staticstype = datastaticsform.cleaned_data["staticstype"]
        staticstype = StaticsTypeDict.objects.get(staticstype=staticstype)
        staticsdatatype = datastaticsform.cleaned_data["staticsdatatype"]
        staticsdatatype = StaticsDataTypeDict.objects.get(staticsdatatype=staticsdatatype)
        if datastaticsid == 0:
            new_staticsdata = ProjectStatistics(statics_num=statics_num,staticsdatatype=staticsdatatype,
                staticstype=staticstype,project_id=projectsingle)
            new_staticsdata.save()
            message = u"新的统计数据添加成功"
        else:
            old_staticsdata = ProjectStatistics.objects.get(content_id=datastaticsid)
            old_staticsdata.statics_num = statics_num
            old_staticsdata.staticstype = staticstype
            old_staticsdata.staticsdatatype = staticsdatatype
            old_staticsdata.save()
            message = u"修改成功"
    else:
        logger.info("datastaticsform Valid Failed"+"**"*10)
        logger.info(datastaticsform.errors)
        message = u"数据没有填完整，请重新填写"
    table = refresh_datastatics_table(request,pid,is_submited) 
    ret={'table':table,'message':message,}
    return simplejson.dumps(ret)

def refresh_datastatics_table(request,pid,is_submited):
    datastatics_list = ProjectStatistics.objects.filter(project_id = pid)
    return render_to_string("widgets/finalreport/final_datastatics_table.html",
                            {        
                                'pid':pid,
                                'datastatics_list':datastatics_list,
                                'is_submited':is_submited,
        })

@dajaxice_register
def datastaticsDelete(request,datastaticsid,pid,is_submited):
    delete_datastatics = ProjectStatistics.objects.get(content_id = datastaticsid)
    delete_datastatics.delete()
    table = refresh_datastatics_table(request,pid,is_submited) 
    ret = {'message':u'删除成功','table':table}
    return simplejson.dumps(ret)

@dajaxice_register
def staticsChange(request,statics_type):
    staticsdatatypedict = StaticsDataTypeDict.objects.filter(staticstype__staticstype = statics_type)
    staticsdatatype_set = []
    for temp in staticsdatatypedict:
        staticsdatatype_set.append(temp.staticsdatatype)
    ret={'staticsdatatype':staticsdatatype_set,}
    return simplejson.dumps(ret)

@dajaxice_register
def fundSummary(request, form, pid):
    profundsummary = ProjectFundSummary.objects.get(project_id = pid) 
    profundsummaryform = ProFundSummaryForm(deserialize_form(form),instance = profundsummary)
    if profundsummaryform.is_valid():
        profundsummaryform.save()
        message = u"保存成功"
    else:
        loginfo(p=profundsummaryform.errors,label='profundsummaryform.errors')
        message = u"保存失败"

    table = refresh_fundsummary_table(request,profundsummaryform,pid)
    ret = {'message':message,'table':table}
    return simplejson.dumps(ret)

def refresh_fundsummary_table(request, profundsummaryform,pid):
    return render_to_string("widgets/finalreport/final_fundsummary_table.html",
                            {        
                                'pid':pid,
                                'profundsummaryform':profundsummaryform,
        })

@dajaxice_register
def createProject(request, title, special):
    teacher = TeacherProfile.objects.get(userid = request.user)
    createNewProject(teacher, title, special)
    return simplejson.dumps({})
@dajaxice_register
def finalReportContent(request,pid,finalsubmitform,is_submited):
    final = FinalSubmit.objects.get( project_id = pid)
    final_form = FinalReportForm(deserialize_form(finalsubmitform),instance=final)
    if final_form.is_valid():
        final_form.save()
        go_next = True
    else:
        go_next = False
        finalsubmitform = refresh_finalsubmit_form(request,final_form,is_submited)
    ret = {'finalsubmitform':finalsubmitform,'go_next':go_next,}
    return simplejson.dumps(ret)

def refresh_finalsubmit_form(request,final_form,is_submited):

    return render_to_string("widgets/finalreport/finalreport_content.html",
                            {        
                                'is_submited':is_submited,
                                'final':final_form,
        })

@dajaxice_register
def finalReportFinish(request,pid):

	project = ProjectSingle.objects.get(project_id = pid)
	finalsubmit = project.finalsubmit
	fundsummary = project.projectfundsummary
	loginfo(p=finalsubmit.project_summary,label="finalsubmit")
	loginfo(p=fundsummary.total_budget,label="fundbudget")
	if finalsubmit.project_summary:
		if fundsummary.total_budget != '0':
			status_confirm(project,FINAL_WEB_CONFIRM)
			message = u"项目状态变为结题书网上提交"
		else:
			message = u"请完善经费决算表内容"
	else:
		message = u"请完善报告正文内容"

	ret = {'message':message,'pid':pid,}
	return simplejson.dumps(ret)
