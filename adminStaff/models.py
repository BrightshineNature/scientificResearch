# coding: UTF-8
import uuid
from backend.utility import make_uuid

from django.db import models
# Create your models here.

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

    # school = models.ForeignKey(SchoolProfile, blank=False, null=False, verbose_name=u"所属学院")

    # student = models.ForeignKey(TeacherProfile, blank=False, null=False, verbose_name=u"教师")

    # expert = models.ManyToManyField(ExpertProfile, through='Re_Project_Expert')

    # project_category = models.ForeignKey(ProjectCategory, verbose_name=u"项目类型",
    #                                      blank=True, null=True, default=None)
    # project_grade = models.ForeignKey(ProjectGrade, verbose_name=u"项目级别",
    #                                   blank=True, null=True, default=None)
    # project_status = models.ForeignKey(ProjectStatus, verbose_name=u"项目状态",
    #                                    blank=True, null=True,
    #                                    default=None)
    # year = models.IntegerField(blank=False, null=False, max_length=4,
    #                            default=lambda: datetime.datetime.today().year,
    #                            verbose_name=u"参加年份")
    # recommend = models.BooleanField(null=False, default=False,
    #                                 verbose_name=u"推荐")
    # is_past = models.BooleanField(null=False, default=False,
    #                               verbose_name=u"往届项目")
    # try:
    #     default_status = OverStatus.objects.get(status=OVER_STATUS_NOTOVER)
    # except:
    #     default_status = 1
    # over_status = models.ForeignKey(OverStatus, verbose_name=u"结束状态",
    #                                 blank=True, null=True,
    #                                    default=default_status)
    # file_application = models.BooleanField(null=False, default=False,
    #                               verbose_name=u"申报书")
    # file_opencheck = models.BooleanField(null=False, default=False,
    #                             verbose_name=u"开题检查表")
    # file_interimchecklist = models.BooleanField(null=False, default=False,
    #                               verbose_name=u"中期检查表")
    # file_summary = models.BooleanField(null=False, default=False,
    #                               verbose_name=u"结题验收")
    # file_projectcompilation = models.BooleanField(null=False, default=False,
    #                               verbose_name=u"项目汇编")
    # score_application = models.BooleanField(null=False, default=False,
    #                               verbose_name=u"学分申请")
    # # is_applicationover = models.BooleanField(null=False, default=False,
    # #                               verbose_name=u"申请结束判断")
    # funds_total   = models.FloatField(blank=False, verbose_name=u"经费总额",
    #                                 default=0)
    # funds_remain  = models.FloatField(blank=False, verbose_name=u"经费余额",
    #                                 default=0)
    # project_code = models.CharField(blank=False, null=True, max_length=14, verbose_name=u"项目申报编号")
    # project_unique_code = models.CharField(blank=True, null=True, default='',
    #                                        max_length=14, verbose_name=u"项目编号")
    # class Meta:
    #     verbose_name = "参赛项目"
    #     verbose_name_plural = "参赛项目"

    # def __unicode__(self):
    #     return self.title
