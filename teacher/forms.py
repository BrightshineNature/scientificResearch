# coding: UTF-8
from django import forms
from django.forms import ModelForm

from teacher.models import *
import datetime
from users.models import Special
from const import *
from common.utility import checkIdcard

class ProjectBudgetInformationForm(forms.Form):
	project_basicexpenses = forms.CharField(required=True,label="基本科研业务费经费",widget=forms.TextInput(attrs={'class':'form-control budgetform',}))
	project_selfexpense = forms.CharField(required=True,label="项目单位自筹经费",widget=forms.TextInput(attrs={'class':'form-control budgetform',}))
	project_totalexpense = forms.CharField(required=True,label="总经费",widget=forms.TextInput(attrs={'class':'form-control budgetform',}))

class ProjectBudgetAnnualForm(forms.Form):
	YEAR_CHOICE = []
	currentyear = datetime.datetime.now().year
	for i in range(currentyear-2,currentyear+3):
		YEAR_CHOICE.append((i,i))	
	year_list = forms.ChoiceField(choices = YEAR_CHOICE,
							   required=True,label="预算年份",widget=forms.Select(attrs={'class':'form-control budgetformselect',}))
	project_budgetfunds = forms.CharField(required=True,label="预算安排经费",widget=forms.TextInput(attrs={'class':'form-control budgetform',}))
	project_previousfunds = forms.CharField(required=True,label="项目以前年度结转经费",widget=forms.TextInput(attrs={'class':'form-control budgetform',}))

class SettingForm(ModelForm):
    """
        Teacher's Setting Information Form
    """
    # def clean_card(self):
    #     card = self.cleaned_data.get("card", "").strip()
    #     response = checkIdcard(card)
    #     if response[0]:
    #         raise forms.ValidationError(response[1])
    #     return card
    class Meta:
        model = TeacherInfoSetting
        exclude = ("teacher", )
        widgets = {"name": forms.TextInput(attrs={"class":'form-control', "placeholder": "姓名", }),
                   "sex": forms.Select(attrs={'class':'form-control', }),
                   "card": forms.TextInput(attrs={"class":'form-control', "placeholder": "身份证号", }),
                   "birth": forms.TextInput(attrs = {"class": "form-control", "placeholder": "出生年月 yyyy-MM"}),
                   "base_name": forms.TextInput(attrs={"class":'form-control', "placeholder": "所在研究基地名称（可为空）", }),
                   "target_type": forms.Select(attrs={'class':'form-control', }),
                   "degree": forms.Select(attrs={'class':'form-control', }),
                   "title": forms.Select(attrs={'class':'form-control', }),
                   "base_type": forms.Select(attrs={'class':'form-control', }),
                   "position": forms.Select(attrs={'class':'form-control', }),
                  }
  
class FinalReportForm(ModelForm):
    """
        Final Form
    """
    class Meta:
        model = FinalSubmit
        #TODO: add css into widgets
        exclude = ('project_id', 'content_id', )
        widgets = {"project_keyword": forms.Textarea(attrs={'rows': 1, 'cols': 100,
                                                                'placeholder':'关键词(不超过5个)',
                                                                'class':"fill-form"},),
                   "project_summary": forms.Textarea(attrs={'rows': 8, 'cols': 100,
                                                                'placeholder': '概括项目精华，如背景、方向、主要内容、重要成果，关键数据及其科学意义等信息,不超过300字',
                                                                'class': "fill-form"}),
                   "project_plan": forms.Textarea(attrs={'rows': 8, 'cols': 100,
                                                                'placeholder':'研究计划要点及执行情况概述...',
                                                                'class': "fill-form"}),
                   "project_progress": forms.Textarea(attrs={'rows': 8, 'cols': 100,
                                                       'placeholder':'研究工作主要进展和所取得的成果...',
                                                       'class': "fill-form"}),
                   "academic_exchange": forms.Textarea(attrs={'rows': 8, 'cols': 100,
                                                       'placeholder':'国内外学术合作交流与人才培养情况(如无,可以不写)...',
                                                       'class': "fill-form"}),
                   "existing_problems": forms.Textarea(attrs={'rows': 8, 'cols': 100,
                                                       'placeholder':'存在的问题、建议及其他需要说明的情况...',
                                                       'class': "fill-form"}),
                   }

class ProjectAchivementForm(forms.Form):
    """
        ProjectAchivementForm
    """

    achivementtitle = forms.CharField(
                                required=True,
                                widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "成果或论文名称", }),)
    mainmember = forms.CharField(
                                required=True,
                                widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "主要完成者", }),)
    introduction = forms.CharField(
                                required=True,
                                widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "成果说明", }),)
    remarks = forms.CharField(
                                required=True,
                                widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "标注状况", }),)
    achivementtype = forms.ChoiceField(choices = ACHIVEMENT_TYPE,
                            required=True,
                            widget=forms.Select(attrs={'class':'form-control search-input final_report_form','placeholder':"成果类型"}),)


class ProjectDatastaticsForm(forms.Form):
    """
        ProjectDatastaticsForm
    """
    staticstype = forms.ChoiceField(choices = STATICS_TYPE,
                            required=True,
                            widget=forms.Select(attrs={'class':'form-control search-input final_report_form','placeholder':"类别"}),)
    staticsdatatype = forms.ChoiceField(choices = STATICS_DATA_TYPE,
                        required=True,
                        widget=forms.Select(attrs={'class':'form-control search-input final_report_form','placeholder':"级别"}),)
    statics_num = forms.CharField(
                                required=True,
                                widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "数量", }),)


class ProFundSummaryForm(ModelForm):
	class Meta:
		model = ProjectFundSummary
		exclude = ('content_id','project_id','finance_comment','equcosts_budget','equcosts_expenditure','finance_account',)
        widgets = {"finance_account": forms.TextInput(attrs={"class":'form-control', "placeholder": "财务账号", }),
                  }

class ProgressForm(ModelForm):
    class Meta:
        model = ProgressReport
        exclude = ('content_id', 'project_id', 'year', )
        widgets = {
            "summary": forms.Textarea(attrs={"rows": "8", "cols": "100", "class":'fill-form', "placeholder": "项目本年取得的成效。填写具体成果获得的阶段性成效，文字不超过300字", }),
 
        }
class ProFundBudgetForm(ModelForm):
	class Meta:
		model = ProjectFundBudget
		exclude = ('content_id','project_id','finance_comment','equcosts_budget',)

class ProjectCreationForm(forms.Form):
    SPECIAL_CHOICE = tuple((special.id, special.name) for special in Special.objects.all())
    title = forms.CharField(
                            required=True,
                            widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "项目名称", }),)
    special = forms.ChoiceField(required = True, choices = SPECIAL_CHOICE, widget = forms.Select(attrs = {"class": "form-control",}))
    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm, self).__init__(*args, **kwargs)
        SPECIAL_CHOICE = tuple((special.id, special.name) for special in Special.objects.filter(application_status = True))
        self.fields["special"].choices = SPECIAL_CHOICE

class ProjectChangeForm(forms.Form):
    project_special=forms.ChoiceField(required=True,choices=(),widget=forms.Select(attrs={"class":"form-control"}))
    def __init__(self, *args,**kwargs):
        special=kwargs.get("special",None)
        if special != None :
            del kwargs['special']            
        super(ProjectChangeForm, self).__init__(*args, **kwargs)
        SPECIAL_CHOICE = [(sp.id, sp.name) for sp in Special.objects.filter(application_status = True)]
        if special != None :
            SPECIAL_CHOICE.remove((special.id,special.name))
            SPECIAL_CHOICE=[(special.id,special.name)]+SPECIAL_CHOICE
        SPECIAL_CHOICE=tuple(SPECIAL_CHOICE)
        self.fields["project_special"].choices = SPECIAL_CHOICE


