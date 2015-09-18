# coding: UTF-8
from django.contrib.auth.models import User
from django.db import models
from const import *

class NewsCategory(models.Model):
    """
    """
    category = models.CharField(blank=False, null=False, unique=True, max_length=20,
                                choices=NEWS_CATEGORY_CHOICES, \
                                default=NEWS_CATEGORY_ANNOUNCEMENT ,
                                verbose_name=u"新闻类型")
    class Meta:
        verbose_name = "新闻类型"
        verbose_name_plural = "新闻类型"

    def __unicode__(self):
        return self.get_category_display()


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
    status = models.IntegerField(blank=False, unique=True,
                              choices=PROJECT_STATUS_CHOICES,
                               verbose_name="项目状态")
    next_status = models.IntegerField(blank=False, unique=True,
                              choices=PROJECT_STATUS_PENDDING,
                               verbose_name="项目下一个状态")
    class Meta:
        verbose_name = "项目状态"
        verbose_name_plural = "项目状态"
    def __unicode__(self):
        return self.get_status_display()
    def get_next_status(self):
        return self.get_next_status_display()
    def get_export_str(self):
        if self.status == PROJECT_STATUS_OVER:
            return u"结题"
        elif self.status == PROJECT_STATUS_STOP:
            return u"终止"
        else:
            return u"在研"

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
class Subject(models.Model):
    """
    Subject
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=SUBJECT_CHOICES,
                                verbose_name="学科代码")
    class Meta:
        verbose_name = "学科"
        verbose_name_plural = "学科"
    def __unicode__(self):
        return self.get_category_display()
class NationalTradeCode(models.Model):
    """
    National Trade Code:
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=NATIONAL_TRADE_CODE_CHOICES,
                                verbose_name="国民行业代码")
    class Meta:
        verbose_name = "国民行业代码"
        verbose_name_plural = "国民行业代码"
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

class AchivementTypeDict(models.Model):
    achivementtype = models.CharField(blank=True,max_length=100,default="0",choices=ACHIVEMENT_TYPE,unique=True,verbose_name=u"成果类型")
    class Meta:
        verbose_name = "成果类型列表"
        verbose_name_plural = "成果类型列表"
    def __unicode__(self):
        return self.get_achivementtype_display()

class StaticsTypeDict(models.Model):
	staticstype = models.CharField(blank=True,max_length=100,choices=STATICS_TYPE,unique=True,verbose_name=u"统计数据类别")
	class Meta:
		verbose_name = "统计数据类别列表"
		verbose_name_plural = "统计数据类别列表"
	
	def __unicode__(self):
		return self.get_staticstype_display()

class StaticsDataTypeDict(models.Model):
    staticsdatatype = models.CharField(blank=True,null=True,max_length=100,choices=STATICS_DATA_TYPE,unique=True,verbose_name=u"统计内容类型")
    staticstype = models.ForeignKey(StaticsTypeDict,blank=False, null=False, verbose_name=u"统计数据级别")
    class Meta:
        verbose_name = "统计数据级别列表"
        verbose_name_plural = "统计数据级别列表"

    def __unicode__(self):            
        return self.get_staticsdatatype_display()

class UserIdentity(models.Model):
    """
    Login User identity: AdminStaff, AdminSystem, Expert, SchoolTeam, visitor,
    Teacher, Student
    """
    identity = models.CharField(max_length=50, blank=False, unique=True,
                                choices=AUTH_CHOICES, default=VISITOR_USER,
                                verbose_name="身份级别")
    auth_groups = models.ManyToManyField(User, related_name="identities")

    class Meta:
        verbose_name = "登录权限"
        verbose_name_plural = "登录权限"

    def __unicode__(self):
        return self.get_identity_display()

class ExpertReview(models.Model):
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=EXPERT_REVIEW_TABLE_CHOICES,
                                verbose_name="专家评审表")
    class Meta:
        verbose_name = "专家评审表"
        verbose_name_plural = "专家评审表"
    def __unicode__(self):
        return self.get_category_display()

class ExpertFinalReview(models.Model):
    
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=EXPERT_FINAL_REVIEW_TABLE_CHOICES,
                                verbose_name="专家评审终审表")
    class Meta:
        verbose_name = "专家评审终审表"
        verbose_name_plural = "专家评审终审表"
    def __unicode__(self):
        return self.get_category_display()

        
class ProfileIdenty(models.Model):
    """
    Subject
    """
    category = models.CharField(max_length=30, blank=False, unique=True,
                                choices=AUTH_CHOICES,
                                verbose_name="身份")
    class Meta:
        verbose_name = "账户身份"
        verbose_name_plural = "账户身份"
    def __unicode__(self):
        return self.get_category_display()
