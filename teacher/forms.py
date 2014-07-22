# coding: UTF-8
from django import forms
from django.forms import ModelForm

from teacher.models import *
import datetime

from const import *


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
    class Meta:
        model = TeacherInfoSetting
        exclude = ("teacher", )
        widgets = {"name": forms.TextInput(attrs={"class":'form-control', "placeholder": "姓名", }),
                   "sex": forms.Select(attrs={'class':'form-control', }),
                   "card": forms.TextInput(attrs={"class":'form-control', "placeholder": "身份证号", }),
                   "birth": forms.TextInput(attrs = {"class": "form-control", "placeholder": "出生年月 yyyy-MM"}),
                   "base_name": forms.TextInput(attrs={"class":'form-control', "placeholder": "所在研究基地名称", }),
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
                                                                'placeholder': '项目摘要',
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




