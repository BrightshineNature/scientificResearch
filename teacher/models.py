# coding: UTF-8

import uuid

from const import *
from django.db import models
from backend.utility import make_uuid
from adminStaff.models import ProjectSingle
from const.models import  AchivementTypeDict,StaticsTypeDict,StaticsDataTypeDict
from users.models import TeacherProfile


class FinalSubmit(models.Model):
    """
    inheribit table, which use ProjectSingle to show final-submit content
    """
    content_id = models.CharField(max_length=50,
                                  primary_key=True, default=lambda: str(uuid.uuid4()),
                                  verbose_name="结题报告唯一ID")
    project_id = models.ForeignKey(ProjectSingle)

    project_keyword = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="关键词")

    project_summary = models.CharField(max_length=500, blank=False, null=True,
                                           verbose_name="项目摘要")
    project_plan = models.TextField(blank=False, null=True,
                                           verbose_name="研究计划要点及执行情况概述")
    project_progress = models.TextField(blank=False, null=True,
                                          verbose_name="研究工作主要进展和所取得的成果")
    academic_exchange = models.TextField(blank=True, null=True,
                                       verbose_name="国内外学术合作交流与人才培养情况")
    existing_problems = models.TextField(blank=False, null=True,
                                       verbose_name="存在的问题、建议")



    class Meta:
        verbose_name = "项目结题报告"
        verbose_name_plural = "项目结题报告"

    def __unicode__(self):
        return self.project_id.title

class ProjectAchivement(models.Model):
    """
    inheribit table, which use ProjectSingle to show final-submit content
    """
    content_id = models.CharField(max_length=50,
                                  primary_key=True, default=lambda: str(uuid.uuid4()),
                                  verbose_name="研究成果唯一ID")
    finalsubmit_id = models.ForeignKey(FinalSubmit)

    achivementtype = models.ForeignKey(AchivementTypeDict)

    achivementtitle = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="成果或论文名称")

    mainmember = models.CharField(max_length=500, blank=False, null=True,
                                           verbose_name="主要完成者")
    introduction = models.CharField(max_length=500, blank=False, null=True,
                                           verbose_name="成果说明")
    remarks = models.CharField(max_length=500, blank=True, null=True,
                                           verbose_name="标注状况")


    class Meta:
        verbose_name = "研究成果"
        verbose_name_plural = "研究成果"

    def __unicode__(self):
        return self.achivementtitle

class TeacherInfoSetting(models.Model):
    teacher = models.OneToOneField(TeacherProfile)
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="姓名")
    card = models.CharField(max_length=100, blank=False, null=True, verbose_name="身份证号码")
    sex  = models.CharField(max_length=100, blank=False, null=True, choices=SEX_CHOICES, verbose_name="性别")
    birth = models.CharField(max_length=100, blank=False, null=True, verbose_name="出生年月")
    base_name = models.CharField(max_length=100, blank=False, null=True, verbose_name="所在研究基地名称")
    target_type = models.CharField(max_length=100, blank=False, null=True, choices=PROJECT_IDENTITY_CHOICES, verbose_name="支持对象")
    degree = models.CharField(max_length=100, blank=False, null=True, choices=DEGREE_CHOICES, verbose_name="学位")
    title = models.CharField(max_length=100, blank=False, null=True, choices=PROFESSIONAL_TITLE_CHOICES, verbose_name="职称")
    base_type = models.CharField(max_length=100, blank=False, null=True, choices=EXECUTIVE_POSITION_CHOICES, verbose_name="所在研究基地类型")
    position = models.CharField(max_length=100, blank=False, null=True, choices=RESEARCH_BASES_TYPE_CHOICES, verbose_name="行政职务")
    
    class Meta:
        verbose_name = "注册信息"
        verbose_name_plural = "注册信息"
    def __unicode__(self):
        return self.name
class ProjectStatistics(models.Model):
    """
    inheribit table, which use ProjectSingle to show final-submit content
    """
    content_id = models.CharField(max_length=50,
                                  primary_key=True, default=lambda: str(uuid.uuid4()),
                                  verbose_name="统计数据唯一ID")
    finalsubmit_id = models.ForeignKey(FinalSubmit)

    staticstype = models.ForeignKey(StaticsTypeDict,blank=False, null=False, verbose_name=u"统计数据类别")

    staticsdatatype = models.ForeignKey(StaticsDataTypeDict,blank=False, null=False, verbose_name=u"统计数据级别")

    statics_num = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="数量")

    class Meta:
        verbose_name = "统计数据"
        verbose_name_plural = "统计数据"

    def __unicode__(self):
        return self.staticsdatatype.__unicode__() + "(" +self.staticstype.__unicode__() + ")"

