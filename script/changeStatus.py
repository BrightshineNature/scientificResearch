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
from common.utility import xls_info_duplicatecheck

projs = ProjectSingle.objects.filter(project_status__gte = PROJECT_STATUS_PROGRESS_WEB_OVER)
for pro in projs:
    print pro.project_status.status
    pstatus = ProjectStatus.object.get(status = pro.project_status.status+1)
    pro.project_status = pstatus
    print pro.project_status.status

# data = xlrd.open_workbook("1.xlsx")
# table = data.sheet_by_index(0)

# for i in range(1,592):
#     print i
#     row = table.row_values(i)
#     print row[3]
#     college=College.objects.get(name= row[3])
#     sendemail('1',row[1],row[1][-6:],row[2],EXPERT_USER,row[0],send_email = False,college=college.id)

# print "hello"

# users = User.objects.filter(username__endswith='x')
# for user in users:
#     u=user.username[:-1]
#     u=u+'X'
#     user.username = u
#     user.save()
#     print u

# print "hello"

# teachers = TeacherInfoSetting.objects.filter(card__endswith='x')
# teachers.count()
# for t in teachers:
#     u=t.card[:-1]
#     u=u+'X'
#     t.card=u
#     t.save()
#     print t.card

# print "hello"

proj_list = ProjectSingle.objects.filter(Q(application_year = 2014) & Q(project_status__status__lt =PROJECT_STATUS_APPROVAL) & Q(project_status__status__gte =PROJECT_STATUS_APPLICATION_COLLEGE_OVER))
xls_info_duplicatecheck("1",proj_list)
print "end"
