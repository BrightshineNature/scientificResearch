# coding: UTF-8
import uuid,datetime, os
from django.db import models
from backend.utility import make_uuid
from settings import MEDIA_ROOT
from settings import NEWS_DOCUMENTS_PATH
from const import *
from users.models import TeacherProfile,CollegeProfile,Special,College
from const.models import ProjectStatus,NewsCategory,ScienceActivityType




class TemplateNoticeMessage(models.Model):
    title = models.CharField(blank=False,max_length=30)
    message = models.TextField(blank=False)
from users.models import SchoolProfile,ExpertProfile
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
                             verbose_name=u"项目名称")
    comment = models.CharField(max_length=400, blank=True,
                             verbose_name=u"评审意见")
    teacher = models.ForeignKey(TeacherProfile, blank=False, null=False, verbose_name=u"项目申请人")
    project_sendback_status = models.ForeignKey(ProjectStatus,blank=False,default=None,verbose_name=u"项目退回状态")
    # expert = models.ManyToManyField(ExpertProfile, through = "Re_Project_Expert")

    try:
        default_status = ProjectStatus.objects.get(status = PROJECT_STATUS_APPLY)
    except:
        default_status = 1
    project_status=models.ForeignKey(ProjectStatus,blank=False,default=default_status,verbose_name=u"项目状态")
    # expert = models.ManyToManyField(ExpertProfile, through='Re_Project_Expert')

    project_special = models.ForeignKey(Special, verbose_name=u"专题类型", blank=True, null=True, default=None)
    application_year = models.IntegerField(blank=False, null=False, max_length=4,default=lambda: datetime.datetime.today().year,verbose_name=u"申请年份")
    approval_year=models.IntegerField(blank=True, null=True, max_length=4,verbose_name=u"立项年份")
    conclude_year = models.IntegerField(blank=True, null=True, max_length=4,verbose_name=u"结题年份")
    submit_date=models.DateField(blank=True,null=True,verbose_name=u"提交日期")
    file_application = models.BooleanField(null=False, default=False,verbose_name=u"申报书")
    file_task = models.BooleanField(null=False, default=False,verbose_name=u"任务书")
    file_interimchecklist = models.BooleanField(null=False, default=False,verbose_name=u"进展报告")
    file_summary = models.BooleanField(null=False, default=False,verbose_name=u"结题书")
    science_type = models.ForeignKey(ScienceActivityType, verbose_name=u'科技活动类型')
    trade_code = models.CharField(blank=True,max_length = 20, verbose_name= u'国民行业代码(国标)')
    subject_name = models.CharField(blank=True,max_length = 20, verbose_name = u'学科名称')
    subject_code = models.CharField(blank=True,max_length = 20, verbose_name=u'学科代码')
    start_time = models.DateField(blank=True,null=True,verbose_name=u'研究开始时间')
    end_time = models.DateField(blank=True,null =True,verbose_name=u'研究结束时间')
    project_tpye =models.CharField(blank=True,max_length = 20, verbose_name = u'项目类型')
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"

    def __unicode__(self):
        return self.title

class Re_Project_Expert(models.Model):
    project = models.ForeignKey(ProjectSingle)
    expert = models.ForeignKey(ExpertProfile)
    is_first_round = models.BooleanField(blank=False, default=False)
    class Meta:
        unique_together = (("project", "expert", ))
        verbose_name = "项目审核分配"
        verbose_name_plural = "项目审核分配"

class News(models.Model):
    news_title = models.CharField(verbose_name = u"标题",
                                  blank=False, max_length=200)
    news_content = models.TextField(verbose_name = u"新闻内容",max_length=NEWS_MAX_LENGTH,
                                    blank=False)
    news_date = models.DateField(verbose_name = u"发表时间",
                                 default=datetime.datetime.today,
                                 blank=True)
    news_category = models.ForeignKey(NewsCategory, verbose_name = u"新闻类型", blank=False, null=True)
    news_document = models.FileField(upload_to=NEWS_DOCUMENTS_PATH, null=True, blank=True)

    def document_name(self):
        return os.path.basename(self.news_document.name)

    def __unicode__(self):
        return self.news_title

    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = "新闻"
