# coding: UTF-8

import os
from users.models import Special,College

def getSpecial(request):

    ret = Special.objects.filter(school_user__userid = request.user)

    return ret
def getCollege(request):

    return College.objects.filter(school_user__userid = request.user)
