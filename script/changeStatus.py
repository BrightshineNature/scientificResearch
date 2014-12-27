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

data = xlrd.open_workbook("1.xlsx")
table = data.sheet_by_index(0)

for i in range(1,592):
    print i
    row = table.row_values(i)
    print row[3]
    college=College.objects.get(name= row[3])
    sendemail('1',row[1],row[1][-6:],row[2],EXPERT_USER,row[0],send_email = False,college=college.id)

print "hello"
