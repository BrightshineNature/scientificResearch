
from django.contrib import admin
from users.models import *

RegisterClass = (SchoolProfile,
                 ExpertProfile,
                 AdminStaffProfile,
                 FinanceProfile,
                 CollegeProfile,
                 TeacherProfile,
                 )
for item in RegisterClass:
    admin.site.register(item)

