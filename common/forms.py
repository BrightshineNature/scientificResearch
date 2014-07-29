# coding: UTF-8

from django import forms
from const import *
from common.utils import get_application_year_choice,get_approval_year_choice,get_status_choice,get_application_status_choice
from common.models import ProjectMember
class ScheduleBaseForm(forms.Form):
    status_choices = get_status_choice()
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


    

    special_choices = (('-1', '专题类型'), ('0', '理科'), ('1', '文科'))
    special = forms.ChoiceField(choices= special_choices,required=False,
        widget=forms.Select(attrs={
            'class':'form-control ',
            
            }),)

    college_choices = (('-1', '学院'), ('0', '计算机'), ('1', '管经'))
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


class ProjectJudgeForm(forms.Form):
    result_choices=(("-1","请审核"),("1","通过"),("0","不通过"))
    judgeresult =forms.ChoiceField(choices=result_choices,required=True,
        widget=forms.Select(attrs={
            'class':'form-control', 
            
            }),
        )
    application_choice=(("网上申请不合格","网上申请不合格"),("申报书不合格","申报书不合格"))
    application=forms.MultipleChoiceField(choices=application_choice,required=False,
                                          widget=forms.CheckboxSelectMultiple())
   
    final_choice=(("网上提交不合格","网上提交不合格"),("结题书不合格"),("结题书不合格"))
    final=forms.MultipleChoiceField(choices=final_choice,required=False,widget=forms.CheckboxSelectMultiple())
    reason=forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control','row':10}))
from users.models import SchoolProfile
from adminStaff.models import ProjectSingle
class NoticeForm(forms.Form):
    
    mail_content=forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','row':'6'}))
    mail_title=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    special=forms.BooleanField(required=False)
    college=forms.BooleanField(required=False)
    teacher=forms.BooleanField(required=False)
    expert=forms.BooleanField(required=False)
    teacher_year=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    teacher_special=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    expert_year=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())
    expert_special=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request",None)
        super(NoticeForm,self).__init__(*args,**kwargs)
        if request == None:return
        if SchoolProfile.objects.filter(userid=request.user).count()>0:
            project_group=ProjectSingle.objects.filter(project_special__school_user__userid=request.user)
            teacher_year_choice=[]
            teacher_year_choice.extend(list(set([ (item.approval_year,item.approval_year) for item in project_group])))
            teacher_year_choice=tuple(teacher_year_choice)
            teacher_special_choice=[]
            teacher_special_choice.extend(list(set([(item.project_special.id,item.project_special.name) for item in project_group])))
            teacher_special_choice=tuple(teacher_special_choice)
            self.fields["teacher_year"].choices=teacher_year_choice
            self.fields["expert_year"].choices=teacher_year_choice
            self.fields["teacher_special"].choices=teacher_special_choice
            self.fields["expert_special"].choices=teacher_special_choice
class ProjectInfoForm(forms.Form):
    project_name = forms.CharField(
        max_length = 20,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control ',            
            'placeholder':u"项目名称"}), )

    science_type_choices = (("-1", "科技活动类型"),) + SCIENCE_ACTIVITY_TYPE_CHOICES
    science_type = forms.ChoiceField(
        choices= science_type_choices,
        required = True,
        widget=forms.Select(attrs={
            'class':'form-control', 
            'style':'margin: 0px!important',
            'placeholder':u"科技活动类型",
            
            }),
        )
    trade_code = forms.CharField(
        max_length = 20,
        required=True,
        widget=forms.TextInput(
            attrs={
            'class':'form-control ',
            'placeholder':u"国民行业代码（国标）"}), )
    subject_name = forms.CharField(
        max_length = 20,
        required=True,
        widget=forms.TextInput(
            attrs={
            'class':'form-control ',
            'placeholder':u"学科名称"}), )
    subject_code = forms.CharField(
        max_length = 20,
        required=True,
        widget=forms.TextInput(
            attrs={
            'class':'form-control ',
            'placeholder':u"学科代码"}), )
    start_time = forms.DateField(
        # max_length = 20,
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
    project_tpye =forms.CharField(
        max_length = 20,
        required=True,
        widget=forms.TextInput(
            attrs={
            'class':'form-control ',
            'placeholder':u"项目类型"}), )

class BasisContentForm(forms.Form):


    basis =forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"研究意义、国内外研究现状及发展动态分析，需结合科学研究发展趋势来论述科学意义；或结合国民经济和社会发展中迫切需要解决的关键科技问题来论述其应用前景。附主要参考文献目录"}), )


   

    content = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"此部分为重点阐述内容"}), )


    plan = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"包括有关方法、技术路线、实验手段、关键技术等说明"}), )

    innovation = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u""}), )

    expect = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"包括拟组织的重要学术交流活动、国际合作与交流计划等"}), )

class BaseConditionForm(forms.Form):

    base = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"与本项目相关的研究工作积累和已取得的研究工作成绩"}), )
    condition = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"包括已具备的实验条件，尚缺少的实验条件和拟解决的途径"}), )
    applicant = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"包括申请人和项目组主要参与者的学历和研究工作简历，近期已发表与本项目有关的主要论著目录和获得学术奖励情况及在本项目中承担的任务。论著目录要求详细列出所有作者、论著题目、期刊名或出版社名、年、卷（期）、起止页码等；奖励情况也须详细列出全部受奖人员、奖励名称等级、授奖年等"}), )
    project = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"申请人和项目组主要参与者正在承担的科研项目情况，要注明项目的名称和编号、经费来源、起止年月、与本项目的关系及负责的内容等"}), )
    progress = forms.CharField(
        max_length = 10000,
        required=False,
        widget=forms.Textarea(
            attrs={
            'rows': 8, 'cols': 120,
            'class':'form-control ',
            'id':'name',
            'placeholder':u"对申请者负责的前一个已结题基本科研业务费专项项目完成情况、后续研究进展及与本申请项目的关系加以详细说明。另附该已结题项目研究工作总结摘要（限500字）和相关成果的详细目录"}), )

class ProjectMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ('name', 'birth_year', 'tel', 'mail', 'professional_title', 'executive_position')
        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control', 'placeholder': "姓名",}),
            'birth_year':forms.DateInput(attrs = {'class':'form-control','placeholder': "出生年份",}),
            'tel':forms.TextInput(attrs = {'class':'form-control','placeholder': "电话",}),
            'mail':forms.TextInput(attrs = {'class':'form-control','placeholder': "邮箱",}),
            'professional_title':forms.Select(attrs = {'class':'form-control','placeholder': "职称",}),
            'executive_position':forms.Select(attrs = {'class':'form-control','placeholder': "行政职务",}),

        }