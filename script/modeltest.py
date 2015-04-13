# coding: UTF-8
from django.db.models import Q
import datetime
from adminStaff.models import ProjectSingle

pro_list = ProjectSingle.objects.filter(projectfundsummary__serial_number__startswith="2015").order_by("projectfundsummary__serial_number")
for pro in pro_list:
    print pro.projectfundsummary.serial_number

pass
