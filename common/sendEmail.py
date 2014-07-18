# coding: UTF-8
@staticmethod
def sendemail(request,username,person_firstname,password,email,identity,send_email=True, **kwargs):
    #判断用户名是否存在存在直接返回
    if not AuthUserExist(email, identity):
        if kwargs.has_key('school_name'):
            create_inactive_user(request,username,person_firstname,password,email,identity,send_email, school_name=kwargs['school_name'])
        else:
            create_inactive_user(request,username,person_firstname,password,email,identity,send_email, expert_insitute=kwargs['expert_insitute'])
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
def create_inactive_user(self,request,
        username,person_firstname,password,email,
        Identity,send_email=True, profile_callback=None, **kwargs):
    """
     Create a new, inactive ``User``, generates a
     ``RegistrationProfile`` and email its activation key to the
     ``User``, returning the new ``User`        TODO: we will custom the USE
    """
    #如果存在用户的话不必进行新建只需对权限表进行操作即可，否则新建用户
    send_mail_flag = True
    if User.objects.filter(username=username).count() == 0:
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = (not send_email) #special treat for expert_import

        new_user.first_name = person_firstname
        new_user.save()
        registration_profile = self.create_profile(new_user)
        registration_profile.save()
        current_site = Site.objects.get_current()
        site_domain=current_site.domain

        if send_email:
            from django.core.mail import send_mail
            subject = render_to_string('registration/activation_email_subject.txt',
                                       {'site':get_current_site(request),
                                        'username':username,
                                        'password':password})

            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            message = render_to_string('registration/activation_email.txt',
                                       {'activation_key':registration_profile.activation_key,
                                        'expiration_days':settings.ACCOUNT_ACTIVATION_DAYS,
                                        'site':site_domain,
                                        'username':username,
                                        'password':password}
                                      )
            logger.error(message)
            #此处加监控标志
            send_mail_flag = send_mail(subject,
                          message,
                          settings.DEFAULT_FROM_EMAIL,
                          [new_user.email])
    else:
        new_user = User.objects.get(email=email)

        #对用户权限写入数据库
    try:
        new_authority = UserIdentity.objects.get(identity=Identity)
        new_authority.auth_groups.add(new_user)
        new_authority.save()
    except:
        pass

    #如果是学校注册 添加学校注册姓名
    if kwargs.has_key('school_name'):
        schoolObj = SchoolDict.objects.get(id = kwargs["school_name"])
        if SchoolProfile.objects.filter(school=schoolObj).count() == 0:
            schoolProfileObj = SchoolProfile(school=schoolObj, userid =new_user)
            schoolProfileObj.save()
            projectperlimits = ProjectPerLimits(school=schoolProfileObj,
                                                number=0,
                                                a_cate_number=0)
            projectperlimits.save()
        else:
            schoolProfileObj = SchoolProfile.objects.get(school=schoolObj)
            schoolProfileObj.userid = new_user
            schoolProfileObj.save()
    #如果是专家的话加上专家的所属学科
    elif kwargs.has_key('expert_insitute'):
        insituteObj = InsituteCategory.objects.get(id=kwargs["expert_insitute"])
        expertProfileObj = ExpertProfile(subject=insituteObj, userid =new_user)
        expertProfileObj.save()
        #学生注册的话直接填写校对应的管理员即可
    else:
        school_staff_name = request.user.username
        school_staff = User.objects.get(username=school_staff_name)
        school_profile = SchoolProfile.objects.get(userid = school_staff)
        student_obj = StudentProfile(user = new_user,school = school_profile)
        student_obj.save()
    if profile_callback is not None:
        profile_callback(user=new_user)
    return new_user,send_mail_flag

def create_profile(self,user):
    """
    Create a ``RegistrationProfile`` for a given
    ``User``, and return the ``RegistrationProfile``.
    """
    salt= sha.new(str(random.random())).hexdigest()[:5]
    activation_key = sha.new(salt+user.username).hexdigest()
    return RegistrationProfile(user=user,
                               activation_key=activation_key)

def delete_expired_users(self):
    """
    Remove expired instances of ``RegistrationProfile`` and their associated ``User``s.

    It is recommended that this method be executed regularly as
    part of your routine site maintenance; this application
    provides a custom management command which will call this
    method, accessible as ``manage.py cleanupregistration``.

    """
    for profile in self.all():
        if profile.activation_key_expired():
            user = profile.user
            if not user.is_active:
                user.delete()
