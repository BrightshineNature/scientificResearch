# coding: UTF-8
from django.db import models

from const import *

class ScienceActivityType(models.Model):
    """
    Science Activity Type:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=SCIENCE_ACTIVITY_TYPE_CHOICES,
                                verbose_name="科技活动类型")
    class Meta:
        verbose_name = "科技活动类型"
        verbose_name_plural = "科技活动类型"
    def __unicode__(self):
        return self.get_category_display()

class ProjectStatus(models.Model):
    """
    Project Status:
    """
    status = models.CharField(max_length=30, blank=False, unique=True,
                              choices=PROJECT_STATUS_CHOICES,
                               verbose_name="项目状态")
    class Meta:
        verbose_name = "项目状态"
        verbose_name_plural = "项目状态"
    def __unicode__(self):
        return self.get_status_display()
class Sex(models.Model):
    """
    Sex:
    """
    choices = models.CharField(max_length=30, blank=False, unique=True,
                               choices=SEX_CHOICES,
                               verbose_name="")
    class Meta:
        verbose_name = "性别"
        verbose_name_plural = "性别"
    def __unicode__(self):
        return self.get_choices_display()
class ProjectIdentity(models.Model):
    """
    Project Identity:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=PROJECT_IDENTITY_CHOICES,
                                verbose_name="支持对象")
    class Meta:
        verbose_name = "支持对象"
        verbose_name_plural = "支持对象"
    def __unicode__(self):
        return self.get_category_display()
class Degree(models.Model):
    """
    Degree:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=DEGREE_CHOICES,
                                verbose_name="学位")
    class Meta:
        verbose_name = "学位"
        verbose_name_plural = "学位"
    def __unicode__(self):
        return self.get_category_display()
class ProfessionalTitle(models.Model):
    """
    Project Title:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=PROFESSIONAL_TITLE_CHOICES,
                                verbose_name="职称")
    class Meta:
        verbose_name = "职称"
        verbose_name_plural = "职称"
    def __unicode__(self):
        return self.get_category_display()
class ExecutivePosition(models.Model):
    """
    Executive Position:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=EXECUTIVE_POSITION_CHOICES,
                                verbose_name="行政职务")
    class Meta:
        verbose_name = "行政职务"
        verbose_name_plural = "行政职务"
    def __unicode__(self):
        return self.get_category_display()
class ResearchBaseType(models.Model):
    """
    Executive Position:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=RESEARCH_BASES_TYPE_CHOICES,
                                verbose_name="所在研究基地类型")
    class Meta:
        verbose_name = "所在研究基地类型"
        verbose_name_plural = "所在研究基地类型"
    def __unicode__(self):
        return self.get_category_display()
