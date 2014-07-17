# coding: UTF-8

import uuid

from django.db import models

from backend.utility import make_uuid

# Create your models here.


class ProjectSingle(models.Model):
    """
    Every single projects, include basic infomation, it is the base table.
    """
    project_id = models.CharField(max_length=50, primary_key=True,
                                  default=make_uuid,
                                  verbose_name=u"题目唯一ID")

    title = models.CharField(max_length=400, blank=False,
                             verbose_name=u"参赛题目")

    class Meta:
        verbose_name = "参赛项目"
        verbose_name_plural = "参赛项目"

    def __unicode__(self):
        return self.title


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

