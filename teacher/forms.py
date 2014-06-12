# coding: UTF-8
from django import forms
import datetime

class ProjectBudgetInformationForm(forms.Form):
	project_basicexpenses = forms.CharField(required=True,label="基本科研业务费经费",widget=forms.TextInput(attrs={'class':'',}))
	project_selfexpense = forms.CharField(required=True,label="项目单位自筹经费",widget=forms.TextInput(attrs={'class':'',}))
	project_totalexpense = forms.CharField(required=True,label="总经费",widget=forms.TextInput(attrs={'class':'',}))

class ProjectBudgetAnnualForm(forms.Form):
	YEAR_CHOICE = []
	currentyear = datetime.datetime.now().year
	print currentyear
	for i in range(currentyear-2,currentyear+3):
		YEAR_CHOICE.append((i,i))	
	year_list = forms.ChoiceField(choices = YEAR_CHOICE,
							   required=True,label="预算年份",widget=forms.Select(attrs={'class':'',}))
	project_budgetfunds = forms.CharField(required=True,label="预算安排经费",widget=forms.TextInput(attrs={'class':'',}))
	project_previousfunds = forms.CharField(required=True,label="项目以前年度结转经费",widget=forms.TextInput(attrs={'class':'',}))
