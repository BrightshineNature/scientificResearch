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

class ProjectFundSummary(models.Model):
    content_id = models.CharField(max_length=50,
   							   primary_key=True, default=lambda: str(uuid.uuid4()),
   							   verbose_name="经费决算表唯一ID")
    finalsubmit_id = models.ForeignKey(FinalSubmit)
   
    finance_comment = models.CharField(max_length=50, blank=True, null=True,default="",
   										verbose_name="财务评审意见")
 
    equcosts_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="设备费预算经费")
    equcosts_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="设备费经费支出")
    equcosts_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="设备费说明")
    equacquisition_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="设备购置费经费")
    equacquisition_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="设备购置费支出")
    equacquisition_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="设备购置费说明")
    equtrial_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="试制改造费经费")
    equtrial_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="试制改造费支出")
    equtrial_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="试制改造费说明")
    equrent_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="设备改造与租赁费预算经费")
    equrent_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="设备改造与租赁费经费支出")
    equrent_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="设备改造与租赁费说明")
    material_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="材料费预算经费")
    material_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="材料费经费支出")
    material_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="材料费说明")
    testcosts_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="测试化验加工费预算经费")
    testcosts_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="测试化验加工费经费支出")
    testcosts_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="测试化验加工费说明")
    fuelpower_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="燃料动力费预算经费")
    fuelpower_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="燃料动力费经费支出")
    fuelpower_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="燃料动力费说明")
    travel_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="差旅费预算经费")
    travel_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="差旅费经费支出")
    travel_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="差旅费说明")
    conference_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="会议费预算经费")
    conference_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="会议费经费支出")
    conference_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="会议费说明")
    cooperation_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="国际合作与交流费预算经费")
    cooperation_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="国际合作与交流费经费支出")
    cooperation_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="国际合作与交流费说明")
    publish_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="出版费预算经费")
    publish_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="出版费经费支出")
    publish_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="出版费说明")
    laborcosts_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="劳务费预算经费")
    laborcosts_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="劳务费经费支出")
    laborcosts_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="劳务费说明")
    expertadvice_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="专家咨询费预算经费")
    expertadvice_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="专家咨询费经费支出")
    expertadvice_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="专家咨询费说明")
    total_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="合计预算经费")
    total_expenditure = models.CharField(max_length=50, blank=False, null=True,default="0",
   										verbose_name="合计经费支出")
    total_remark = models.CharField(max_length=100, blank=False, null=True,
   										verbose_name="合计说明")
   
   
    class Meta:
   	 verbose_name = "经费决算表"
   	 verbose_name_plural = "经费决算表"
   
    def __unicode__(self):
   	 return self.finalsubmit_id.project_id.__unicode__()

class ProjectFundBudget(models.Model):
    content_id = models.CharField(max_length=50,
                                  primary_key=True, default=lambda: str(uuid.uuid4()),
                                  verbose_name="经费预算表唯一ID")
    finalsubmit_id = models.ForeignKey(FinalSubmit)
   
    equcosts_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="设备费预算经费")
    equcosts_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="设备费说明")
    equacquisition_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="设备购置费经费")
    equacquisition_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="设备购置费说明")
    equtrial_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="试制改造费经费")
    equtrial_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="试制改造费说明")
    equrent_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="设备改造与租赁费预算经费")
    equrent_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="设备改造与租赁费说明")
    material_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="材料费预算经费")
    material_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="材料费说明")
    testcosts_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="测试化验加工费预算经费")
    testcosts_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="测试化验加工费说明")
    fuelpower_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="燃料动力费预算经费")
    fuelpower_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="燃料动力费说明")
    travel_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="差旅费预算经费")
    travel_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="差旅费说明")
    conference_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="会议费预算经费")
    conference_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="会议费说明")
    cooperation_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="国际合作与交流费预算经费")
    cooperation_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="国际合作与交流费说明")
    publish_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="出版费预算经费")
    publish_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="出版费说明")
    laborcosts_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="劳务费预算经费")
    laborcosts_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="劳务费说明")
    expertadvice_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="专家咨询费预算经费")
    expertadvice_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="专家咨询费说明")
    total_budget = models.CharField(max_length=50, blank=False, null=True,default="0",
                                           verbose_name="合计预算经费")
    total_remark = models.CharField(max_length=100, blank=False, null=True,
                                           verbose_name="合计说明")
    finance_comment = models.CharField(max_length=50, blank=True, null=True,default="",
                                           verbose_name="财务评审意见")
   
   
    class Meta:
        verbose_name = "经费预算表"
        verbose_name_plural = "经费预算表"
   
    def __unicode__(self):
        return self.finalsubmit_id.project_id.__unicode__()
   
