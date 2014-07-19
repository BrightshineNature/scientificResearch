# coding: UTF-8
import uuid
from backend.utility import make_uuid
from users.models import TeacherProfile,SchoolProfile
from const.models import ProjectStatus
from const import *
from django.db import models
import datetime
# Create your models here.

class Special(models.Model):

    school_user = models.ForeignKey(SchoolProfile, blank=True, null=False, verbose_name=u"专题管理员")    
    name = models.CharField(blank=False,max_length=30)
    def __unicode__(self):
        return self.name

class TemplateNoticeMessage(models.Model):
    title = models.CharField(blank=False,max_length=30)
    message = models.TextField(blank=False)

class ProjectSingle(models.Model):
    """
    Every single projects, include basic infomation, it is the base table.
    """
    project_id = models.CharField(max_length=50, primary_key=True,
                                  default=make_uuid,
                                  verbose_name=u"题目唯一ID")

    project_application_code = models.CharField(blank=False, null=True, max_length=14, verbose_name=u"项目申报编号")

    project_code = models.CharField(blank=True, null=True, default='',max_length=14, verbose_name=u"项目编号")

    title = models.CharField(max_length=400, blank=False,
                             verbose_name=u"参赛题目")

    school = models.ForeignKey(SchoolProfile, blank=False, null=False, verbose_name=u"所属学院")

    teacher = models.ForeignKey(TeacherProfile, blank=False, null=False, verbose_name=u"项目申请人")

    project_status=models.ForeignKey(ProjectStatus,blank=False,default=PROJECT_STATUS_APPLY,verbose_name=u"项目状态")
    # expert = models.ManyToManyField(ExpertProfile, through='Re_Project_Expert')

    project_special = models.ForeignKey(Special, verbose_name=u"专题类型", blank=True, null=True, default=None)
    application_year = models.IntegerField(blank=False, null=False, max_length=4,default=lambda: datetime.datetime.today().year,verbose_name=u"申请年份")
    approval_year=models.IntegerField(blank=True, null=True, max_length=4,verbose_name=u"立项年份")
    submit_date=models.DateField(blank=True,null=True,verbose_name=u"提交日期")
    file_application = models.BooleanField(null=False, default=False,verbose_name=u"申报书")
    file_task = models.BooleanField(null=False, default=False,verbose_name=u"任务书")
    file_interimchecklist = models.BooleanField(null=False, default=False,verbose_name=u"进展报告")
    file_summary = models.BooleanField(null=False, default=False,verbose_name=u"结题书")
    class Meta:
        verbose_name = "参赛项目"
        verbose_name_plural = "参赛项目"

    def __unicode__(self):
        return self.title

