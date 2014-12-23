# coding: UTF-8
from adminStaff.models import ProjectSingle
from const.models import ProjectStatus
from users.models import College
from const import *
from backend.logging import loginfo
from common.sendEmail import sendemail

import xlrd

data = xlrd.open_workbook("1.xls")
table = data.sheet_by_index(0)

row = table.row_values(2)

college=College.objects.get(name= row[3])
print college.id
sendemail('1',row[1],row[1][-6:],row[2],TEACHER_USER,row[0],send_email = False,college=college.id)
