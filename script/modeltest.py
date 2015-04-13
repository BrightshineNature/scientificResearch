# coding: UTF-8
from django.db.models import Q
import datetime
from adminStaff.models import ProjectSingle

pro_list = ProjectSingle.objects.filter(projectfundsummary__serial_number__startswith="2015")
print pro_list.count()
