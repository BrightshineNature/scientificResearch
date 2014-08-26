# coding: UTF-8

import os
from users.models import Special,College
from backend.decorators import check_auth
def getSpecial(request):
    specials = []
    if check_auth(request.user,request.session.get('auth_role', "")):
        specials = Special.objects.filter(school_user__userid = request.user)
    return specials

def getCollege(request):
    colleges = []
    if check_auth(request.user,request.session.get('auth_role', "")):
        colleges = College.objects.filter(school_user__userid = request.user)
    return colleges
