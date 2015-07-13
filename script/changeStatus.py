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


data = xlrd.open_workbook("1.xls")
table = data.sheet_by_index(0)

for i in range(371,692):
    row = table.row_values(i)
    pro=ProjectSingle.objects.get(project_code = row[14])
    try:
        pro.trade_code = NationalTradeCode.objects.get(category = NATIONAL_TRADE_CODE_DICTS[row[16]])
        pro.save()
    except:
        print i
    # college=College.objects.get(name= row[3])
    # sendemail('1',row[1],row[1][-6:],row[2],TEACHER_USER,row[0],send_email = True,college=college.id)
    # teacher= TeacherProfile.objects.get(userid__username = row[1])
    # teacherInfoSettingObj  = TeacherInfoSetting.objects.get(teacher = teacher.id)
    # teacherInfoSettingObj.sex  = SEX_DICTS[row[4]]
    # teacherInfoSettingObj.birth = row[5]
    # teacherInfoSettingObj.base_name = row[11]
    # teacherInfoSettingObj.target_type = PROJECT_IDENTITY_DICTS[row[6]]
    # teacherInfoSettingObj.degree = DEGREE_DICTS[row[7]]
    # teacherInfoSettingObj.title = PROFESSIONAL_TITLE_DICTS[row[8]]
    # teacherInfoSettingObj.base_type = RESEARCH_BASES_TYPE_DICTS[row[10]]
    # teacherInfoSettingObj.position = EXECUTIVE_POSITION_DICTS[row[9]]
    # teacherInfoSettingObj.save()
    # special = Special.objects.get(name = row[22])
    # project = createNewProject(teacher,row[13],special.id)
    # print project
    # project.project_code = unicode(row[14])
    # project.project_budget_max = float(row[23])*10000
    # project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_TASK_SCHOOL_OVER)
    # # if int(int(row[20])) <=2013:
    # #
    # # else:
    # #     project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_TASK_SCHOOL_OVER)
    # project.application_year = 2014
    # project.approval_year = 2014
    # project.start_time = datetime.datetime.strptime(row[19],"%Y-%m")
    # project.end_time = datetime.datetime.strptime(row[20],"%Y-%m")
    # project.science_type = ScienceActivityType.objects.get(category = SCIENCE_ACTIVITY_TYPE_DICTS[row[15]])
    # # project.trade_code = NationalTradeCode.objects.get(category = NATIONAL_TRADE_CODE_DICTS[row[16]])
    # project.subject = Subject.objects.get(category = SUBJECT_DICTS[int(row[18])])
    # project.save()
    # sendemail('1',row[1],row[1][-6:],row[2],EXPERT_USER,row[0],send_email = False,college=college.id)

print "hello"
# projs = ProjectSingle.objects.filter(Q(project_status__gte = PROJECT_STATUS_APPLICATION_REVIEW_START) & Q(project_status__lt = PROJECT_STATUS_APPROVAL))
# pstatus = ProjectStatus.objects.get(status=PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT)
# print pstatus
# print projs.count()
# for pro in projs:
#     pro.project_status = pstatus
#     pro.save()

# print "hello"
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

# proj_list = ProjectSingle.objects.filter(Q(application_year = 2014) & Q(project_status__status__lt =PROJECT_STATUS_APPROVAL) & Q(project_status__status__gte =PROJECT_STATUS_APPLICATION_COLLEGE_OVER))
# xls_info_duplicatecheck("1",proj_list)
# print "end"
