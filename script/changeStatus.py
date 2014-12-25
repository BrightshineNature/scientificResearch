# coding: UTF-8
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

import xlrd

data = xlrd.open_workbook("1.xls")
table = data.sheet_by_index(0)

for i in range(2,3):
    print i
    row = table.row_values(i)
    print row[3]
    college=College.objects.get(name= row[3])
    sendemail('1',row[1],row[1][-6:],row[2],TEACHER_USER,row[0],send_email = True,college=college.id)
    teacher= TeacherProfile.objects.get(userid__username = row[1])
    teacherInfoSettingObj  = TeacherInfoSetting.objects.get(teacher = teacher.id)
    teacherInfoSettingObj.sex  = SEX_DICTS[row[4]]
    teacherInfoSettingObj.birth = row[5]
    teacherInfoSettingObj.base_name = row[11]
    teacherInfoSettingObj.target_type = PROJECT_IDENTITY_DICTS[row[6]]
    teacherInfoSettingObj.degree = DEGREE_DICTS[row[7]]
    teacherInfoSettingObj.title = PROFESSIONAL_TITLE_DICTS[row[8]]
    teacherInfoSettingObj.base_type = RESEARCH_BASES_TYPE_DICTS[row[10]]
    teacherInfoSettingObj.position = EXECUTIVE_POSITION_DICTS[row[9]]
    teacherInfoSettingObj.save()
    special = Special.objects.get(name = row[22])
    project = createNewProject(teacher,row[13],special.id)
    print project
    project.project_code = unicode(row[14])
    project.project_budget_max = float(row[23])*10000
    if int(int(row[20])) <=2013:
        project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_PROGRESS_SCHOOL_OVER)
    else:
        project.project_status = ProjectStatus.objects.get(status = PROJECT_STATUS_TASK_SCHOOL_OVER)
    project.application_year = int(row[20])
    project.approval_year = int(row[20])
    project.start_time = datetime.datetime.strptime(row[18],"%Y-%m")
    project.end_time = datetime.datetime.strptime(row[19],"%Y-%m")
    project.science_type = ScienceActivityType.objects.get(category = SCIENCE_ACTIVITY_TYPE_DICTS[row[15]])
    # project.trade_code = NationalTradeCode.objects.get(category = NATIONAL_TRADE_CODE_DICTS[row[16]])
    project.subject = Subject.objects.get(category = SUBJECT_DICTS[int(row[17])])
    project.save()

print "hello"
