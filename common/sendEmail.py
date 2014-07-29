# coding: UTF-8
from django.contrib.auth.models import User
from const.models import UserIdentity
from registration.models import RegistrationManager
def sendemail(request,username,password,email,identity,person_firstname,send_email=True, **kwargs):
    #判断用户名是否存在存在直接返回
    if not AuthUserExist(username, identity,person_firstname):
        RegistrationManager().create_inactive_user(request,username,password,email,identity,person_firstname,send_email,**kwargs)
        return True
    else:
        return False
def AuthUserExist(username, identity,person_firstname):
    if User.objects.filter(username=username).count():
        user_obj = User.objects.get(username=username)
        ui_obj = UserIdentity.objects.get(identity=identity)
        if ui_obj.auth_groups.filter(id=user_obj.id).count():
            return True
        elif user_obj.first_name != person_firstname:
            return True
        else:
            return False
    else:
        return False
