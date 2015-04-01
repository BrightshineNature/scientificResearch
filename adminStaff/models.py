# coding: UTF-8
import uuid,datetime, os
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import settings

from backend.utility import make_uuid
from settings import MEDIA_ROOT
from settings import NEWS_DOCUMENTS_PATH
from const import *
from django.contrib.auth.models import User
from users.models import TeacherProfile,CollegeProfile,Special,College,SchoolProfile,ExpertProfile
from const.models import ProjectStatus,NewsCategory,ScienceActivityType,NationalTradeCode,Subject,ProfileIdenty




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
                             verbose_name=u"项目名称")
    comment = models.CharField(max_length=400, blank=True,null=True,
                             verbose_name=u"评审意见")
    teacher = models.ForeignKey(TeacherProfile, blank=False, null=False, verbose_name=u"项目申请人")
    # expert = models.ManyToManyField(ExpertProfile, through = "Re_Project_Expert")

    try:
        default_status = ProjectStatus.objects.get(status = PROJECT_STATUS_APPLY)
    except:
        default_status = 1
    project_status=models.ForeignKey(ProjectStatus,blank=False,default=default_status,verbose_name=u"项目状态")
    project_sendback_status = models.ForeignKey(ProjectStatus,verbose_name=u"项目退回状态",blank=True,null=True,default=None)

    project_special = models.ForeignKey(Special, verbose_name=u"专题类型", blank=True, null=True, default=None)
    application_year = models.IntegerField(blank=False, null=False, max_length=4,default=lambda: datetime.datetime.today().year,verbose_name=u"申请年份")
    approval_year=models.IntegerField(blank=True, null=True, max_length=4,verbose_name=u"立项年份")
    conclude_year = models.IntegerField(blank=True, null=True, max_length=4,verbose_name=u"结题年份")
    submit_date=models.DateField(blank=True,null=True,default=lambda: datetime.datetime.today(),verbose_name=u"提交日期")
    file_application = models.BooleanField(null=False, default=False,verbose_name=u"申报书")
    file_task = models.BooleanField(null=False, default=False,verbose_name=u"任务书")
    file_interimchecklist = models.BooleanField(null=False, default=False,verbose_name=u"进展报告")
    file_summary = models.BooleanField(null=False, default=False,verbose_name=u"结题书")
    science_type = models.ForeignKey(ScienceActivityType,verbose_name=u'科技活动类型',blank=True,null=True)
    trade_code = models.ForeignKey(NationalTradeCode,verbose_name= u'国民行业代码(国标)',blank=True,null=True)
    subject = models.ForeignKey(Subject,verbose_name = u'学科',blank=True,null=True)
    start_time = models.DateField(blank=True,null=True,
        # default=lambda: datetime.datetime.today(),
        verbose_name=u'研究开始时间')
    end_time = models.DateField(blank=True,null =True,
        # default=lambda: datetime.datetime.today(),
        verbose_name=u'研究结束时间')
    project_tpye =models.CharField(blank=True,null=True,max_length = 20, verbose_name = u'项目类型')
    project_budget_max = models.IntegerField(blank = False, default = 0, verbose_name = u"项目最大预算金额")
    finance_account = models.CharField(max_length = 20,blank = True,null = True, verbose_name="财务账号")
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"

    def __unicode__(self):
        return self.title
    def get_next_status(self):
        if self.project_special.review_status:
            pendding_dict = PROGRESS_REVIEW_DICT
        else:
            pendding_dict = PROGRESS_NOT_REVIEW_DICT
        return pendding_dict[self.project_status.status][PENDDING_STATUS]

class ReviewBackView(models.Model):
    userid = models.ForeignKey(User,verbose_name="权限对应ID")
    comment = models.CharField(max_length=400, blank=True,null=True,verbose_name=u"评审意见")
    identy = models.ForeignKey(ProfileIdenty,verbose_name=u'身份',blank=True,null=True)
    class Meta:
        verbose_name = "评审退回意见"
        verbose_name_plural = "评审退回意见"

    def __unicode__(self):
        return self.title
class Re_Project_Expert(models.Model):
    project = models.ForeignKey(ProjectSingle)
    expert = models.ForeignKey(ExpertProfile)
    is_first_round = models.BooleanField(blank=False, default=False)
    class Meta:
        unique_together = (("project", "expert","is_first_round"))
        verbose_name = "项目审核分配"
        verbose_name_plural = "项目审核分配"
    def __unicode__(self):
        s = u"初审" if self.is_first_round else u"终审"
        return "%s_%s_%s" % (s, self.expert, self.project)

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



class BasicScientificResearchScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    summary = models.IntegerField(blank = False, default = 0, verbose_name = u"研究计划要点和执行情况概述（10分）", validators = [MaxValueValidator(10), MinValueValidator(0)])
    completion = models.IntegerField(blank = False, default = 0, verbose_name = u"立项考核指标及完成情况（30分）", validators = [MaxValueValidator(30), MinValueValidator(0)])
    achievement = models.IntegerField(blank = False, default = 0, verbose_name = u"研究工作主要进展和取得的成果（40分）", validators = [MaxValueValidator(40), MinValueValidator(0)])
    prospect = models.IntegerField(blank = False, default = 0, verbose_name = u"重大项目培育科研专题科研项目下一步研究计划和谋划重大项目的工作思路（10分）", validators = [MaxValueValidator(10), MinValueValidator(0)])
    funds_report = models.IntegerField(blank = False, default = 0, verbose_name = u"经费使用情况汇报（10分）", validators = [MaxValueValidator(10), MinValueValidator(0)])
    class Meta:
        verbose_name = u"基本科研业务费重大项目培育科研专题项目评审表"
        verbose_name_plural = u"基本科研业务费重大项目培育科研专题项目评审表"
    def get_total_score(self):
        return self.summary + self.completion + self.achievement + self.prospect + self.funds_report
    def get_comments(self):
        return ""

    @staticmethod
    def has_comments():
        return -1

class HumanitiesSocialSciencesResearchScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    significance = models.IntegerField(blank = False, default = 0, verbose_name = u"研究意义（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    innovation = models.IntegerField(blank = False, default = 0, verbose_name = u"研究内容及创新性（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    feasibility = models.IntegerField(blank = False, default = 0, verbose_name = u"研究方案及可行性（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    base = models.IntegerField(blank = False, default = 0, verbose_name = u"研究基础与工作条件（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    class Meta:
        verbose_name = u"基本科研业务费人文社科科研专题一般项目评审表"
        verbose_name_plural = u"基本科研业务费人文社科科研专题一般项目评审表"
    def get_total_score(self):
        return self.significance + self.innovation + self.feasibility + self.base
    def get_comments(self):
        return ""
    @staticmethod
    def has_comments():
        return -1



class ScienceFoundationResearchScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    check = models.IntegerField(blank = False, default = 0, verbose_name = u"是否理科基础科研（100分）", validators = [MaxValueValidator(100), MinValueValidator(0)])
    score = models.IntegerField(blank = False, default = 0, verbose_name = u"评分（100分）", validators = [MaxValueValidator(100), MinValueValidator(0)])
    class Meta:
        verbose_name = u"基本科研业务费理科基础科研专题一般项目评审表"
        verbose_name_plural = u"基本科研业务费理科基础科研专题一般项目评审表"
    def get_total_score(self):
        return self.score
    def get_comments(self):
        return str(self.check)
    @staticmethod
    def has_comments():
        return 0



class FrontAndIntercrossResreachScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    score = models.IntegerField(blank = False, default = 0, verbose_name = u"评分（100分）", validators = [MaxValueValidator(100), MinValueValidator(0)])
    level = models.IntegerField(blank = False, default = 0, choices = LEVEL_CHOICES[:3], verbose_name = u"对所评内容熟悉程度")
    class Meta:
        verbose_name = u"基本科研业务费前沿探索与学科交叉科研专题一般项目评审表"
        verbose_name_plural = u"基本科研业务费前沿探索与学科交叉科研专题一般项目评审表"
    def get_total_score(self):
        return self.score
    def get_comments(self):
        return str(self.get_level_display())
    @staticmethod
    def has_comments():
        return 1



 
class OutstandingYoungResreachScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    score = models.IntegerField(blank = False, default = 0, verbose_name = u"评分（100分）", validators = [MaxValueValidator(100), MinValueValidator(0)])
    level = models.IntegerField(blank = False, default = 0, choices = LEVEL_CHOICES[:4], verbose_name = u"优先资助级别")
    class Meta:
        verbose_name = u"基本科研业务费优秀青年人才科研专题一般项目评审表"
        verbose_name_plural = u"基本科研业务费优秀青年人才科研专题一般项目评审表"
    def get_total_score(self):
        return self.score
    def get_comments(self):
        return str(self.get_level_display())
    @staticmethod
    def has_comments():
        return 1

class MajorProjectScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    evaluation = models.IntegerField(blank = False, default = 0, verbose_name = u"项目成果及前景评价（20分）", validators = [MaxValueValidator(20), MinValueValidator(0)])
    feasibility = models.IntegerField(blank = False, default = 0, verbose_name = u"工作计划可行性（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    funds_report = models.IntegerField(blank = False, default = 0, verbose_name = u"经费使用情况（10分）", validators = [MaxValueValidator(10), MinValueValidator(0)])
    expection = models.IntegerField(blank = False, default = 0, verbose_name = u"预期成果合理性（20分）", validators = [MaxValueValidator(20), MinValueValidator(0)])
    measures = models.IntegerField(blank = False, default = 0, verbose_name = u"为实现考核目标所采取的措施（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    class Meta:
        verbose_name = u"重大项目培育科研专题项目评审表"
        verbose_name_plural = u"重大项目培育科研专题项目评审表"
    def get_total_score(self):
        return self.evaluation + self.feasibility + self.funds_report + self.expection + self.measures
    def get_comments(self):
        return ""
    @staticmethod
    def has_comments():
        return -1



class KeyLaboratoryProjectScoreTable(models.Model):
    re_obj = models.ForeignKey(Re_Project_Expert)
    significance = models.IntegerField(blank = False, default = 0, verbose_name = u"立项意义（25分）", validators = [MaxValueValidator(25), MinValueValidator(0)])
    innovation = models.IntegerField(blank = False, default = 0, verbose_name = u"研究内容及创新性（30分）", validators = [MaxValueValidator(30), MinValueValidator(0)])
    feasibility = models.IntegerField(blank = False, default = 0, verbose_name = u"研究方案及可行性（20分）", validators = [MaxValueValidator(20), MinValueValidator(0)])
    base = models.IntegerField(blank = False, default = 0, verbose_name = u"研究基础与工作条件（15分）", validators = [MaxValueValidator(15), MinValueValidator(0)])
    funds_report = models.IntegerField(blank = False, default = 0, verbose_name = u"经费是否合理（10分）", validators = [MaxValueValidator(10), MinValueValidator(0)])
    class Meta:
        verbose_name = u"重点实验室专题项目评审表"
        verbose_name_plural = u"重点实验室专题项目评审表"
    def get_total_score(self):
        return self.significance + self.innovation + self.feasibility + self.base + self.funds_report
    def get_comments(self):
        return ""
    @staticmethod
    def has_comments():
        return -1



class HomePagePic(models.Model):
    """
    """
    pic_obj = models.FileField(upload_to=settings.HOMEPAGE_PIC_PATH,
                               verbose_name="文件对象")
    name = models.CharField(max_length=100, blank=False,
                            verbose_name="文件名称")
    uploadtime = models.DateTimeField(blank=True, null=True,
                                      verbose_name="上传时间")
    file_size = models.CharField(max_length=50, blank=True, null=True,
                                 default=None, verbose_name="文件大小")
    file_type = models.CharField(max_length=50, blank=True, null=True,
                                 default=None, verbose_name="文件类型")
    class Meta:
        verbose_name = "首页图片上传"
        verbose_name_plural = "首页图片上传"

    def __unicode__(self):
        return self.name
    def file_name(self):
        return os.path.basename(self.file_obj.name)
