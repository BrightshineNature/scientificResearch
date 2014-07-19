# coding: UTF-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form

from django.http import Http404
from django.utils import simplejson
from teacher.forms import *
from teacher.models import *
from const.models import *
from backend.logging import logger, loginfo
from django.template.loader import render_to_string
@dajaxice_register
def achivementChange(request,form,achivementid,finalsubmitid):

    achivementform = ProjectAchivementForm(deserialize_form(form))
    finalsubmit = FinalSubmit.objects.get(content_id=finalsubmitid)
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
                achivementtype=achivementtype,finalsubmit_id=finalsubmit)
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
    table = refresh_achivement_table(request,finalsubmit) 
    ret={'table':table,'message':message,}
    return simplejson.dumps(ret)


def refresh_achivement_table(request,finalsubmit):
    achivement_list = ProjectAchivement.objects.filter(finalsubmit_id = finalsubmit.content_id)
    return render_to_string("widgets/finalreport/final_achivement_table.html",
                            {        
                                'finalreportid':finalsubmit.content_id,
                                'achivement_list':achivement_list,
        })

@dajaxice_register
def achivementDelete(request,achivementid,finalsubmitid):
    finalsubmit = FinalSubmit.objects.get(content_id=finalsubmitid)
    delete_achivement = ProjectAchivement.objects.get(content_id = achivementid)
    delete_achivement.delete()
    table = refresh_achivement_table(request,finalsubmit) 
    ret = {'message':u'删除成功','table':table}
    return simplejson.dumps(ret)

@dajaxice_register
def datastaticsChange(request,form,datastaticsid,finalsubmitid):

    datastaticsform = ProjectDatastaticsForm(deserialize_form(form))
    finalsubmit = FinalSubmit.objects.get(content_id=finalsubmitid)
    message=""
    if datastaticsform.is_valid():
        statics_num = datastaticsform.cleaned_data["statics_num"]
        staticstype = datastaticsform.cleaned_data["staticstype"]
        staticstype = StaticsTypeDict.objects.get(staticstype=staticstype)
        staticsdatatype = datastaticsform.cleaned_data["staticsdatatype"]
        staticsdatatype = StaticsDataTypeDict.objects.get(staticsdatatype=staticsdatatype)
        if datastaticsid == 0:
            new_staticsdata = ProjectStatistics(statics_num=statics_num,staticsdatatype=staticsdatatype,
                staticstype=staticstype,finalsubmit_id=finalsubmit)
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
    table = refresh_datastatics_table(request,finalsubmit) 
    ret={'table':table,'message':message,}
    return simplejson.dumps(ret)

def refresh_datastatics_table(request,finalsubmit):
    datastatics_list = ProjectStatistics.objects.filter(finalsubmit_id = finalsubmit.content_id)
    return render_to_string("widgets/finalreport/final_datastatics_table.html",
                            {        
                                'finalreportid':finalsubmit.content_id,
                                'datastatics_list':datastatics_list,
        })

@dajaxice_register
def datastaticsDelete(request,datastaticsid,finalsubmitid):
    finalsubmit = FinalSubmit.objects.get(content_id=finalsubmitid)
    delete_datastatics = ProjectStatistics.objects.get(content_id = datastaticsid)
    delete_datastatics.delete()
    table = refresh_datastatics_table(request,finalsubmit) 
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