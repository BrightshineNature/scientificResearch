# coding: UTF-8
from backend.logging import logger
from django.db import models
from django.contrib.auth.models import User
from const.models import UserIdentity,ExpertReview
from const import ADMINSTAFF_USER,SCHOOL_USER,COLLEGE_USER,TEACHER_USER,EXPERT_USER,FINANCE_USER,VISITOR_USER


from const.models import ExpertFinalReview
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

    department = models.CharField(blank=False,max_length=30,verbose_name=u"部门名称")
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

class Special(models.Model):
    school_user = models.ForeignKey(SchoolProfile, blank=True, null=True, verbose_name=u"专题管理员")
    try:
        default_status = ExpertReview.objects.get(category = EXPERT_REVIEW_HUMANITIESSOCIAL)
    except:
        default_status = 2
    expert_review = models.ForeignKey(ExpertReview, blank=False, null=False, default=default_status,verbose_name=u"专家评审表")


    expert_final_review = models.ForeignKey(ExpertFinalReview, blank=True, null=True,verbose_name=u"专家评审终审表")

    
    name = models.CharField(blank=False,max_length=30)
    review_status = models.BooleanField(blank=True,default=True)
    alloc_status = models.BooleanField(blank=True,default= False)
    final_alloc_status = models.BooleanField(blank=True,default= False)
    application_status = models.BooleanField(blank=True,default= False)
    task_status = models.BooleanField(blank=True,default= False)
    progress_status = models.BooleanField(blank=True,default= False)
    final_status = models.BooleanField(blank=True,default= False)
    class Meta:
        verbose_name = "专题"
        verbose_name_plural = "专题"
    def __unicode__(self):
        return self.name





class College(models.Model):
    college_user = models.ForeignKey(CollegeProfile, blank=True, null=True, verbose_name=u"学院管理员")
    name = models.CharField(blank=False,max_length=30)
    class Meta:
        verbose_name = "学院"
        verbose_name_plural = "学院"
    def __unicode__(self):
        return self.name


class ExpertProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")
    college = models.ForeignKey(College,
                               verbose_name="所属学院")
    class Meta:
        verbose_name = "评审专家"
        verbose_name_plural = "评审专家"

    def __unicode__(self):
        return '%s' % (self.userid.first_name)

    def save(self, *args, **kwargs):
        super(ExpertProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=EXPERT_USER)
        self.userid.identities.add(auth)

class TeacherProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")
    college = models.ForeignKey(College,
                               verbose_name="所属学院")
    class Meta:
        verbose_name = "教师"
        verbose_name_plural = "教师"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(TeacherProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=TEACHER_USER)
        self.userid.identities.add(auth)
