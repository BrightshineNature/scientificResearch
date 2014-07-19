# coding: UTF-8
import re,sha,random,uuid
from django.db import transaction
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import get_current_site,Site
from backend.logging import logger
from django.db import models
from django.contrib.auth.models import User
from const.models import UserIdentity
from django.contrib.sites.models import get_current_site,Site
from const import ADMINSTAFF_USER,SCHOOL_USER,COLLEGE_USER,TEACHER_USER,EXPERT_USER,FINANCE_USER,VISITOR_USER
SHA1_RE = re.compile('^[a-f0-9]{40}$')      #Activation Key
class AdminStaffProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = "管理员"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(AdminStaffProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=ADMINSTAFF_USER)
        self.userid.identities.add(auth)

class FinanceProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")

    class Meta:
        verbose_name = "财务管理员"
        verbose_name_plural = "财务管理员"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(FinanceProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=FINANCE_USER)
        self.userid.identities.add(auth)


class SchoolProfile(models.Model):
    """
    User Profile Extend
    The Administrator can modify them in admin.page
    """
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")

    class Meta:
        verbose_name = "专题管理员"
        verbose_name_plural = "专题管理员"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(SchoolProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=SCHOOL_USER)
        self.userid.identities.add(auth)

class CollegeProfile(models.Model):
    """
    User Profile Extend
    The Administrator can modified them in admin.page
    """
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")

    class Meta:
        verbose_name = "学院秘书"
        verbose_name_plural = "学院秘书"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(CollegeProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=COLLEGE_USER)
        self.userid.identities.add(auth)


class ExpertProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")
    class Meta:
        verbose_name = "评审专家"
        verbose_name_plural = "评审专家"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(ExpertProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=EXPERT_USER)
        self.userid.identities.add(auth)

class TeacherProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")
    # school = models.ForeignKey(SchoolDict, unique=True, verbose_name="学校名称")
    class Meta:
        verbose_name = "教师"
        verbose_name_plural = "教师"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(TeacherProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=TEACHER_USER)
        self.userid.identities.add(auth)

class RegistrationManager(models.Manager):
    """
    Custom manager for ``RegistrationProfile`` model.

    The methods defined here provide shortcuts for account creation
    and activation (including generation and emailing of activation
    keys), and for cleaning out expired inactive accounts.

    """
    @transaction.commit_on_success
    def activate_user(self, activation_key):
        """
        Validate an activation key and activation the corresponding User if vaild.
        """
        if SHA1_RE.search(activation_key):
            try:
                profile = RegistrationProfile.objects.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False
            if not profile.activation_key_expired():
                user = profile.user
                user.is_active = True
                user.save()
                profile.activation_key = "ALREADY_ACTIVATED"
                profile.save()
                return user

        return False
    @transaction.commit_on_success
    def create_inactive_user(self,request,
                             username,person_firstname,password,email,
                             Identity,send_email=True, profile_callback=None, **kwargs):
        """
        Create a new, inactive ``User``, generates a
        ``RegistrationProfile`` and email its activation key to the
        ``User``, returning the new ``User``.

        TODO: we will custom the USER

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
            site_domain =current_site.domain

            if send_email:
                from django.core.mail import send_mail
                subject = render_to_string('email/activation_email_subject.txt',
                                       {'site':get_current_site(request),
                                        'username':username,
                                        'password':password})

                # Email subject *must not* contain newlines
                subject = ''.join(subject.splitlines())
                message = render_to_string('email/activation_email.txt',
                                       {'activation_key':registration_profile.activation_key,
                                        'expiration_days':settings.ACCOUNT_ACTIVATION_DAYS,
                                        'site':site_domain,
                                        'username':username,
                                        'password':password})
                logger.error(message)
                #此处加监控标志
                send_mail_flag = send_mail(subject,
                                           message,
                                           settings.DEFAULT_FROM_EMAIL,
                                           [new_user.email])
        else:
            new_user = User.objects.get(username=username)

        #对用户权限写入数据库
        try:
            new_authority = UserIdentity.objects.get(identity=Identity)
            new_authority.auth_groups.add(new_user)
            new_authority.save()
        except:
            pass

        if Identity == SCHOOL_USER:
            schoolProfileObj = SchoolProfile(userid = new_user)
            schoolProfileObj.save()
        elif Identity == COLLEGE_USER:
            collegeProfileObj = CollegeProfile(userid = new_user)
            collegeProfileObj.save()
        elif Identity == TEACHER_USER:
            teacherProfileObj = TeacherProfile(userid = new_user)
            teacherProfileObj.save()
            teacherInfoSettingObj = TeacherInfoSetting(teacher= teacherProfileObj)
            teacherInfoSettingObj.save()
        elif Identity == EXPERT_USER:
            expertProfileObj = ExpertProfile(userid = new_user)
            expertProfileObj.save()
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

class RegistrationProfile(models.Model):
    """
    A simple profile which stores an activation key for use during user account registration
    """
    user = models.ForeignKey(User,unique=True,verbose_name=_('user'))
    activation_key = models.CharField(_('activation key'), max_length=40)

    objects = RegistrationManager()

    class Meta:
        verbose_name = '激活码管理'
        verbose_name_plural = '激活码管理'

    def __unicode__(self):
        return u"Registration information for %s" % self.user

    def activation_key_expired(self):
        """
        Determine whether this ``RegistrationProfile``'s activation
        key has expired, returning a boolean -- ``True`` if the key
        has expired.
        """
        expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return self.activation_key == "ALREADY_ACTIVATED" or \
               (self.user.date_joined + expiration_date <= datetime.datetime.now())

    activation_key_expired.boolean = True
