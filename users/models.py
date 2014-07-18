# coding: UTF-8
from django.db import models
from django.contrib.auth.models import User
from const.models import UserIdentity
from const import ADMINSTAFF_USER,SCHOOL_USER,COLLEGE_USER,TEACHER_USER,EXPERT_USER,FINANCE_USER,VISITOR_USER

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
        super(SchoolProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=SCHOOL_USER)
        self.userid.identities.add(auth)


class ExpertProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")
    # school = models.ForeignKey(SchoolDict, unique=True, verbose_name="学校名称")
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
