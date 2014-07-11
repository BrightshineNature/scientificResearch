# coding: UTF-8
from django.db import models
from const import ACHIVEMENT_TYPE,STATICS_TYPE,STATICS_PRIZE_TYPE,STATICS_PAPER_TYPE,STATICS_PATENT_TYPE,STATICS_SCHOLAR_TYPE
# Create your models here.

class AchivementTypeDict(models.Model):
	achivementType = models.CharField(blank=True,null=True,max_length=100,choices=ACHIVEMENT_TYPE,unique=True,verbose_name=u"成果类型")
	class Meta:
		verbose_name = "成果类型列表"
		verbose_name_plural = "成果类型列表"
	
	def __unicode__(self):
		return self.get_achivementType_display()

class StaticsTypeDict(models.Model):
	staticsType = models.CharField(blank=True,null=True,max_length=100,choices=STATICS_TYPE,unique=True,verbose_name=u"统计数据类型")
	class Meta:
		verbose_name = "统计数据类型列表"
		verbose_name_plural = "统计数据类型列表"
	
	def __unicode__(self):
		return self.get_staticsType_display()

class StaticsPrizeTypeDict(models.Model):
	staticsPrizeType = models.CharField(blank=True,null=True,max_length=100,choices=STATICS_PRIZE_TYPE,unique=True,verbose_name=u"统计获奖类型")
	class Meta:
		verbose_name = "统计获奖类型列表"
		verbose_name_plural = "统计获奖类型列表"
	
	def __unicode__(self):
		return self.get_staticsPrizeType_display()

class StaticsPaperTypeDict(models.Model):
	staticsPaperType = models.CharField(blank=True,null=True,max_length=100,choices=STATICS_PAPER_TYPE,unique=True,verbose_name=u"统计专著论文类型")
	class Meta:
		verbose_name = "统计专著论文类型列表"
		verbose_name_plural = "统计专著论文类型列表"
	
	def __unicode__(self):
		return self.get_staticsPaperType_display()

class StaticsPatentTypeDict(models.Model):
	staticsPatentType = models.CharField(blank=True,null=True,max_length=100,choices=STATICS_PATENT_TYPE,unique=True,verbose_name=u"统计获奖类型")
	class Meta:
		verbose_name = "统计专利及其他类型列表"
		verbose_name_plural = "统计专利及其他类型列表"
	
	def __unicode__(self):
		return self.get_staticsPatentType_display()

class StaticsScholarTypeDict(models.Model):
	staticsScholarType = models.CharField(blank=True,null=True,max_length=100,choices=STATICS_SCHOLAR_TYPE,unique=True,verbose_name=u"统计人才培养类型")
	class Meta:
		verbose_name = "统计人才培养类型列表"
		verbose_name_plural = "统计人才培养类型列表"
	
	def __unicode__(self):
		return self.get_staticsScholarType_display()
