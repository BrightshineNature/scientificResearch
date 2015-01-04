#coding:UTF-8
# Create your models here.
from const import *
from adminStaff.models import ProjectSingle
import uuid,datetime, os


from django.db import models
from django.db.models import Model, TextField
from const.models import ScienceActivityType
from const.models import ProfessionalTitle,ExecutivePosition

class ProjectMember(Model):

    project = models.ForeignKey(ProjectSingle, blank = True, null = True)
    name = models.CharField(blank = False, null = True, max_length = 20, verbose_name=u'姓名')
    card = models.CharField(max_length=100, blank=False, null=True, verbose_name="身份证号码")
    birth_year = models.IntegerField(blank= False,null=True, max_length = 4, verbose_name=u'出生年份')
    tel = models.CharField(blank = False, null = True, max_length = 20, verbose_name=u'电话')
    mail = models.EmailField(blank = False, null = True, max_length = 100, verbose_name=u'邮箱')
    professional_title = models.ForeignKey(ProfessionalTitle, null = True, verbose_name=u'职称')
    executive_position = models.ForeignKey(ExecutivePosition, null = True, verbose_name=u'行政职务')

class BasisContent(Model):

    project = models.ForeignKey(ProjectSingle, blank = True, null = True)
    basis = TextField(blank = False, null = True, max_length = 10000,verbose_name=u'项目摘要')
    content = TextField(blank = True, null = True, max_length = 10000,verbose_name=u'项目的研究内容、研究目标,以及拟解决的关键科学问题')
    plan = TextField(blank = True, null = True, max_length = 10000,verbose_name=u'拟采取的研究方案及可行性分析')
    innovation = TextField(blank = True, null = True, max_length = 10000,verbose_name=u'本项目的特色与创新之处')
    expect = TextField(blank = True, null = True, max_length = 10000,verbose_name=u'年度研究计划及预期研究结果')

class BaseCondition(Model):

    project = models.ForeignKey(ProjectSingle, blank = True, null = True)
    base = TextField(blank = False, null = True, max_length = 10000,verbose_name=u'工作基础')
    condition = TextField(blank = False, null = True, max_length = 10000,verbose_name=u'工作条件')
    applicant = TextField(blank = False, null = True, max_length = 10000,verbose_name=u'申请人简介')
    research = TextField(blank = False, null = True, max_length = 10000,verbose_name=u'承担科研项目情况')
    progress = TextField(blank = False, null = True, max_length = 10000,verbose_name=u'完成本专项项目情况')

import settings
import time
class UploadFile(Model):

    project = models.ForeignKey(ProjectSingle)
    name = models.CharField(max_length=100, blank=False, verbose_name="文件名称")
    file_obj = models.FileField(upload_to=settings.PROCESS_FILE_PATH +"/%Y/%m/%d",verbose_name="文件对象")
    upload_time = models.DateTimeField(blank=True, null=True,verbose_name="上传时间")
    file_size = models.CharField(max_length=50, blank=True, null=True,default=None, verbose_name="文件大小")
    file_type = models.CharField(max_length=50, blank=True, null=True,default=None, verbose_name="文件类型")

    class Meta:
        verbose_name = "文件上传"
        verbose_name_plural = "文件上传"

    def __unicode__(self):
        return self.name 


