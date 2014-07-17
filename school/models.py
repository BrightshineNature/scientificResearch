# coding: UTF-8
from django.db import models

# Create your models here.
class SchoolProfile(models.Model):
    schoolID=models.CharField(max_length=50,primary_key=True,verbose_name=u"学院编号")
    schoolName=models.CharField(max_length=50,null=False)
    def __unicode__(self):
        return '%s' % self.schoolName
