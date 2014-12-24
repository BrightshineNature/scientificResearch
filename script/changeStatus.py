# coding: UTF-8
from adminStaff.models import ProjectSingle
from const.models import ProjectStatus
from const import *

pro_list = ProjectSingle.objects.filter(project_status__status=PROJECT_STATUS_TASK_COMMIT_OVER )
prostatus = ProjectStatus.objects.get(status=PROJECT_STATUS_FINAL_COMMIT_OVER)
for pro in pro_list:
    pro.project_status = prostatus
    pro.save()

print "aaaa"
