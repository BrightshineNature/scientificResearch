# coding: UTF-8

from django import forms
from const import *
from django.db.models import Q
from backend.logging import loginfo
from common.utils import get_application_year_choice,get_approval_year_choice,get_status_choice,get_application_status_choice,get_conclude_year_choices,get_all_status_choice
from common.models import ProjectMember, BasisContent, BaseCondition
from users.models import Special,College,CollegeProfile

class AllStatusForm(forms.Form):
    status_choices=PROJECT_STATUS_CHOICES
    allstatus=forms.ChoiceField(choices=status_choices,required=False,widget=forms.Select(attrs={'class':'form-control'}))
class ScheduleBaseForm(forms.Form):
    status_choices = get_all_status_choice()
    application_status_choice =get_application_status_choice()
    status_choices = tuple( [(-1, u"项目状态")] + status_choices)
    application_status_choices=get_application_status_choice()
    application_status_choices=tuple([(-1,u"项目状态")]+application_status_choices)
    status =forms. ChoiceField(choices=status_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control', 
            }),
        )
    application_status =forms. ChoiceField(choices=application_status_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control', 
            }),
        )
    application_year_choices = get_application_year_choice()
    application_year = forms.ChoiceField(choices =  application_year_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control' ,
            }),)
    approval_year_choices = get_approval_year_choice()
    approval_year = forms.ChoiceField(choices =  approval_year_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control' ,
            }),)
    conclude_year_choices=get_conclude_year_choices()
    conclude_year = forms.ChoiceField(choices =  conclude_year_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control' ,
            }),)
    special_choices=tuple([("-1",u"专题类型")]+[(item.id,item.name) for item in Special.objects.all()])
    special = forms.ChoiceField(choices= special_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control ',
            }),)
    college_choices =tuple ([('-1', '学院')]+ [(item.id,item.name)for item in College.objects.all()])
    college = forms.ChoiceField(choices = college_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control',
            }),)
    other_search= forms.CharField(
        max_length = 20,
        required=False,
        widget=forms.TextInput(
            attrs={
            'class':'form-control ',
            'id':'name',
            'placeholder':u"输入其他检索关键字"}), )
    def __init__(self,*args,**kwargs):
        request  = kwargs.get("request",None)
        if request != None:
            del kwargs['request']
        super(ScheduleBaseForm, self).__init__(*args, **kwargs)
        if request != None:
            identity = request.session.get('auth_role', "")
            if identity == SCHOOL_USER:
                obj_list = Special.objects.filter(school_user__userid = request.user)
                choice_list=[]
                choice_list.append((-1,"专题类型"))
                for obj in obj_list:
                    choice_list.append((obj.id, obj.name))
                obj_choice = tuple(choice_list)
                loginfo(obj_choice)
                self.fields["special"].choices = obj_choice
            elif identity == COLLEGE_USER:
                obj_list = College.objects.filter(college_user__userid = request.user)
                choice_list=[]
                choice_list.append((-1,"学院"))
                for obj in obj_list:
                    choice_list.append((obj.id, obj.name))
                obj_choice = tuple(choice_list)
                self.fields["college"].choices = obj_choice
                college_status_choices=get_status_choice()
                college_status_choices = tuple( [(-1, u"项目状态")] + college_status_choices)
                self.fields["status"].choices=college_status_choices


class ProjectJudgeForm(forms.Form):
    result_choices=(("-1","请审核"),("1","通过"),("0","不通过"))
    judgeresult =forms.ChoiceField(choices=result_choices,required=True,
        widget=forms.Select(attrs={
            'class':'form-control', 
            }),
        )
    application_choice=((u"网上申请不合格",u"网上申请不合格"),(u"申报书不合格",u"申报书不合格"))
    application=forms.MultipleChoiceField(choices=application_choice,required=False,
                                          widget=forms.CheckboxSelectMultiple())
    final_choice=((u"网上提交不合格",u"网上提交不合格"),(u"结题书不合格",u"结题书不合格"))
    final=forms.MultipleChoiceField(choices=final_choice,required=False,widget=forms.CheckboxSelectMultiple())
    reason=forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control','row':10}))
    max_budget = forms.IntegerField(max_value=50,required=False,widget=forms.DateInput(attrs={'class':'form-control',"onkeyup":"if(this.value.length==1){this.value=this.value.replace(/[^1-9]/g,'')}else{this.value=this.value.replace(/\D/g,'')}" ,'onafterpaste':"if(this.value.length==1){this.value=this.value.replace(/[^1-9]/g,'')}else{this.value=this.value.replace(/\D/g,'')}"}))

from users.models import SchoolProfile
from adminStaff.models import ProjectSingle
from adminStaff.utility import getSpecial

def getTeacherYearGroup(request):
    # return []
    if request.session.get('auth_role', "") == SCHOOL_USER:
        project_group=ProjectSingle.objects.filter(Q(project_special__school_user__userid=request.user) & Q(project_status__status__gte = PROJECT_STATUS_APPROVAL))
    elif request.session.get('auth_role', "") == ADMINSTAFF_USER:
        project_group=ProjectSingle.objects.filter(Q(project_status__status__gte = PROJECT_STATUS_APPROVAL))
    else:
        project_group=ProjectSingle.objects.none()

    # if not project_group:
    #     return tuple((-1, "立项年度"), )
    teacher_year_choice=[]
    teacher_year_choice.extend(list(set([ (item.approval_year,item.approval_year) for item in project_group] )))
    print "JJFJJJ***" * 10
    print teacher_year_choice    

    if not teacher_year_choice:
        tt = (-1, "立项年度")

        return (tt,  )

    teacher_year_choice[0] = (-1, "立项年度")
    teacher_year_choice=tuple(teacher_year_choice)
    return teacher_year_choice
def getSpecialTypeGroup(request):
    special_list = getSpecial(request)
    special_choice_list=[]
    special_choice_list.append((-1,"专题类型"))
    for s in special_list:
        special_choice_list.append((s.id, s.name))
    special_choice_list = tuple(special_choice_list)
    return special_choice_list

class NoticeForm(forms.Form):

    expert_special_select = forms.ChoiceField(required=False,
        widget=forms.Select(attrs={
            'class':'form-control ',
            'style':"width:300px",
            }),)
    teacher_special_select = forms.ChoiceField(required=False,
        widget=forms.Select(attrs={
            'class':'form-control ',
            'style':"width:300px",
            }),)

    teacher_year_select = forms.ChoiceField(required=False,
        widget=forms.Select(attrs={
            'class':'form-control ',
            'style':"width:300px",
            }),)


    expert_list=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())


    mail_content=forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','row':'6'}))
    mail_title=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    special=forms.BooleanField(required=False)
    college=forms.BooleanField(required=False)
    teacher=forms.BooleanField(required=False)
    expert=forms.BooleanField(required=False)
    college_list=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    teacher_year=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    teacher_special=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    expert_year=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    expert_special=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request",None)



        super(NoticeForm,self).__init__(*args,**kwargs)

        

        special_list = getSpecial(request)
        special_choice_list=[]
        special_choice_list.append((-1,"专题类型"))
        for s in special_list:
            special_choice_list.append((s.id, s.name))
        special_choice = tuple(special_choice_list)

        print '&*@' * 20
        print special_choice_list
        self.fields["expert_special_select"].choices = getSpecialTypeGroup(request)

        self.fields["teacher_special_select"].choices = getSpecialTypeGroup(request)
        self.fields["teacher_year_select"].choices = getTeacherYearGroup(request)






        

        if request == None:return
        if SchoolProfile.objects.filter(userid=request.user).count()>0:
            college_list_choice=[]
            college_list_all = CollegeProfile.objects.all()
            for item in college_list_all:
                collegename = [obj.name for obj in item.college_set.all()]
                cname = ""
                for name in collegename:
                    cname=cname+name+'  '
                collegename = item.userid.first_name+'('+cname+')'
                college_list_choice.append((item.id,collegename,))
            college_list_choice=list(set(college_list_choice))

            #college_list_choice.extend(list(set([(item.id,item.userid.first_name) for item in CollegeProfile.objects.all()])))
            project_group=ProjectSingle.objects.filter(project_special__school_user__userid=request.user)
            teacher_year_choice=[]
            teacher_year_choice.extend(list(set([ (item.approval_year,item.approval_year) for item in project_group])))
            teacher_year_choice=tuple(teacher_year_choice)
            teacher_special_choice=[]
            teacher_special_choice.extend(list(set([(item.project_special.id,item.project_special.name) for item in project_group])))
            teacher_special_choice=tuple(teacher_special_choice)

            self.fields["college_list"].choices=college_list_choice
            self.fields["teacher_year"].choices=teacher_year_choice
            self.fields["expert_year"].choices=teacher_year_choice
            self.fields["teacher_special"].choices=teacher_special_choice
            self.fields["expert_special"].choices=teacher_special_choice

            

            
class ProjectInfoForm(forms.Form):
    project_name = forms.CharField(
        max_length = 400,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control ', 

            'placeholder':u"项目名称"}), )

    science_type_choices = (("-1", "---------"),) + SCIENCE_ACTIVITY_TYPE_CHOICES
    science_type = forms.ChoiceField(
        choices= science_type_choices,
        required = True,
        widget=forms.Select(attrs={
            'class':'form-control',
            'style':'width:170px',
            'placeholder':u"科技活动类型",
            }),
        )



    trade_code_choices = (("-1", "---------"),) + NATIONAL_TRADE_CODE_CHOICES
    trade_code = forms.ChoiceField(
        choices= trade_code_choices,
        required = True,
        widget=forms.Select(attrs={
            'class':'form-control',
            # 'style':'margin: 0px!important',
            'style':'width:170px',
            'placeholder':u"国民行业代码（国标）",
            }),
        )
    subject_choices  = (("-1", "---------"),) + SUBJECT_CHOICES
    subject = forms.ChoiceField(
        choices= subject_choices,
        required = True,
        widget=forms.Select(attrs={
            'class':'form-control',
            # 'style':'margin: 0px!important',
            'placeholder':u"学科代码",
            'style':'width:170px',
            }),
        )

    start_time = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
            'class':'form-control ',
            'placeholder':u"研究开始时间"}), )

    end_time = forms.DateField(
        # max_length = 20,
        required=True,
        widget=forms.DateInput(
            attrs={
            'class':'form-control ',
            'placeholder':u"研究结束时间"}), )
    def clean_science_type(self):
        i = self.cleaned_data['science_type'] 
        # print "*" * 100
        try: 
            if i == "-1":
                raise
        except:
            raise forms.ValidationError("SB")
        return i

    def clean_trade_code(self):
        i = self.cleaned_data['trade_code'] 
        # print "*" * 100
        try:        
            if i == "-1":
                raise
        except:
            raise forms.ValidationError("SB")
        return i

    def clean_subject(self):
        i = self.cleaned_data['subject'] 
        # print "*" * 100
        try:        
            if i == "-1":
                raise
        except:
            raise forms.ValidationError("SB")
        return i

class BasisContentForm(forms.ModelForm):

    class Meta:
        model = BasisContent
        fields = ('basis',
         # 'content', 'plan', 'innovation', 'expect'
         )
        widgets = {
        'basis':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"项目研究内容、目标、预期成果等信息，不超过500字",}),
        # 'content':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"此部分为重点阐述内容",}),
        # 'plan':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"包括有关方法、技术路线、实验手段、关键技术等说明",}),
        # 'innovation':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"",}),
        # 'expect':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"包括拟组织的重要学术交流活动、国际合作与交流计划等",}),

        }

class BaseConditionForm(forms.ModelForm):

    class Meta:
        model = BaseCondition
        fields = ('base', 'condition', 'applicant', 'research', 'progress')
        widgets = {
        'base':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"与本项目相关的研究工作积累和已取得的研究工作成绩",}),
        'condition':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"包括已具备的实验条件，尚缺少的实验条件和拟解决的途径",}),
        'applicant':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"包括申请人和项目组主要参与者的学历和研究工作简历，近期已发表与本项目有关的主要论著目录和获得学术奖励情况及在本项目中承担的任务。论著目录要求详细列出所有作者、论著题目、期刊名或出版社名、年、卷（期）、起止页码等；奖励情况也须详细列出全部受奖人员、奖励名称等级、授奖年等",}),
        'research':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"申请人和项目组主要参与者正在承担的科研项目情况，要注明项目的名称和编号、经费来源、起止年月、与本项目的关系及负责的内容等",}),
        'progress':forms.Textarea(attrs = {'rows': 8, 'cols': 120,'class':'form-control', 'placeholder': u"对申请者负责的前一个已结题基本科研业务费专项项目完成情况、后续研究进展及与本申请项目的关系加以详细说明。另附该已结题项目研究工作总结摘要（限500字）和相关成果的详细目录",}),

        }

from common.utility import checkIdcard

class ProjectMemberForm(forms.ModelForm):
    # def clean_card(self):
    #     card = self.cleaned_data.get("card", "").strip()
    #     response = checkIdcard(card)
    #     if response[0]:
    #         raise forms.ValidationError(response[1])
    #     return card

    class Meta:
        model = ProjectMember
        fields = ('project', 'name', 'birth_year', 'tel', 'mail', 'professional_title', 'executive_position', 'card',)
        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control', 'placeholder': "姓名",}),
            'birth_year':forms.DateInput(attrs = {'class':'form-control','placeholder': "出生年份",}),
            'tel':forms.TextInput(attrs = {'class':'form-control','placeholder': "电话",}),
            'mail':forms.TextInput(attrs = {'class':'form-control','placeholder': "邮箱",}),
            'professional_title':forms.Select(attrs = {'class':'form-control','placeholder': "职称",}),
            'executive_position':forms.Select(attrs = {'class':'form-control','placeholder': "行政职务",}),
            'card':forms.TextInput(attrs = {'class':'form-control ', \
                                            'style': 'width:120%;',\
                                            'placeholder': "身份证号码",}),

        }



class EmailForm(forms.Form):
    special =forms. ChoiceField(required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    mail_content=forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','row':'6'}))
    mail_title=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    def __init__(self,*args,**kwargs):
        request = kwargs.get("request",None)
        if request != None:
            del kwargs['request']
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields["special"].choices = [(obj.id,obj.name) for obj in Special.objects.filter(school_user__userid = request.user)]
