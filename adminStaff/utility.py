# coding: UTF-8

import os
from users.models import Special,College

def getSpecial(user):

    ret = Special.objects.filter(school_user__userid = user)

    print "in getSpecial"
    # print ret
    return ret
def getCollege(user):

    return College.objects.filter(school_user__userid = user)
