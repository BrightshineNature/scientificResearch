# coding: UTF-8
from django.db.models import Q
import datetime
from adminStaff.models import ProjectSingle
from const.models import *
from users.models import College,TeacherProfile,Special
from common.models import *
from teacher.models import *
from const import *
from backend.logging import loginfo
from common.sendEmail import sendemail
from common.utils import createNewProject
from django.contrib.auth.models import User
from teacher.models import TeacherInfoSetting
import xlrd
from common.utility import xls_info_conclusionresult

pro_set = ProjectSingle.objects.filter(Q(approval_year = "2013"))
print pro_set.count()
xls_info_conclusionresult(1,pro_set)
