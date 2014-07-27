#coding:UTF-8
# Create your models here.



from const import *
from adminStaff.models import ProjectSingle



from django.db import models
from django.db.models import Model
from const.models import ScienceActivityType
from const.models import ProfessionalTitle,ExecutivePosition

# class ProjectInfo(Model):

#     project = models.ForeignKey(ProjectSingle)

#     project_name = models.CharField( max_length = 50, verbose_name=u'项目名称')


#     # science_type = models.CharField( max_length = 50, verbose_name=u'项目名称')
#     science_type_choices =  SCIENCE_ACTIVITY_TYPE_CHOICES

#     science_type = models.ForeignKey(ScienceActivityType, max_length= 20,
#         choices= science_type_choices,
#         verbose_name=u'科技活动类型')

#     trade_code = models.CharField( max_length = 20, verbose_name= u'国民行业代码(国标)')

#     subject_name = models.CharField( max_length = 20, verbose_name = u'学科名称')

#     subject_code = models.CharField( max_length = 20, verbose_name=u'学科代码')

#     start_time = models.CharField( max_length = 20, verbose_name=u'研究开始时间')

#     end_time = models.CharField( max_length = 20, verbose_name=u'研究结束时间')

#     project_tpye =models.CharField( max_length = 20, verbose_name = u'项目类型')


class ProjectMember(Model):

    project = models.ForeignKey(ProjectSingle, null = True)
    name = models.CharField(blank = False, null = True, max_length = 20, verbose_name=u'姓名')
    birth_year = models.DateField(blank= False,null=True,default=lambda: datetime.datetime.today(),verbose_name=u'出生年份')
    tel = models.CharField(blank = False, null = True, max_length = 20, verbose_name=u'电话')
    mail = models.CharField(blank = False, null = True, max_length = 20, verbose_name=u'邮箱')    
    professional_title = models.ForeignKey(ProfessionalTitle, null = True, verbose_name=u'职称')
    executive_position = models.ForeignKey(ExecutivePosition, null = True, verbose_name=u'行政职务')

