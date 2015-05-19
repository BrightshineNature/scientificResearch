# coding: UTF-8
from django.db.models import Q
import datetime
from adminStaff.models import ProjectSingle

pro_list = ProjectSingle.objects.order_by('approval_year').values('approval_year').distinct()
print len(pro_list)
for pro in pro_list:
    print pro['approval_year']

pass
