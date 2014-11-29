# coding: UTF-8

import os
from const import *
from users.models import Special,College
from backend.decorators import check_auth
def getSpecial(request):
    specials = []
    if request.session.get('auth_role', "") == SCHOOL_USER:
        specials = Special.objects.filter(school_user__userid = request.user)
    elif request.session.get('auth_role', "") in (FINANCE_USER,ADMINSTAFF_USER,COLLEGE_USER):
        specials = Special.objects.all()
    return specials

def getCollege(request):
    colleges = []
    if request.session.get('auth_role', "") == COLLEGE_USER:
        colleges = College.objects.filter(college_user__userid = request.user)
    elif request.session.get('auth_role', "") in  (FINANCE_USER,ADMINSTAFF_USER,SCHOOL_USER):
        colleges = College.objects.all()
    return colleges
