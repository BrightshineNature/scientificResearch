# coding: UTF-8
import re,sha
from django.contrib.auth.models import User
from const.models import UserIdentity
from user.models import *
SHA1_RE = re.compile('^[a-f0-9]{40}$')      #Activation Key
@staticmethod
def sendemail(request,username,person_firstname,password,email,identity,send_email=True, **kwargs):
    #判断用户名是否存在存在直接返回
    if not AuthUserExist(username, identity):
        RegistrationManager().create_inactive_user(request,username,person_firstname,password,email,identity,send_email)
        return True
    else:
        return False
@staticmethod
def AuthUserExist(username, identity):
    if User.objects.filter(username=username).count():
        user_obj = User.objects.get(username=username)
        ui_obj = UserIdentity.objects.get(identity=identity)
        if ui_obj.auth_groups.filter(id=user_obj.id).count():
            return True
        else:
            return False
    else:
        return False
