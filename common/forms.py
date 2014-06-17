# coding: UTF-8

from django import forms
from const import *
class ScheduleBaseForm(forms.Form):
    status_choices = list(PROJECT_STATUS)


    status_choices = tuple( [(-1, u"结题状态")] + status_choices)


    status = forms.ChoiceField(choices=status_choices, 
        widget=forms.Select(attrs={'class':'form-control col-lg-3',}),
        )

    year_choices = (('-1', u"立项年度"), ('0', '2013'), ('1', '2014'),)
    year = forms.ChoiceField(choices =  year_choices,
        widget=forms.Select(attrs={'class':'form-control col-lg-3'  ,}),)


    

    special_choices = (('-1', '专题类型'), ('0', '理科'), ('1', '文科'))
    special = forms.ChoiceField(choices= special_choices,
        widget=forms.Select(attrs={'class':'form-control col-lg-3',}),)



    teacher_name = forms.CharField(
        max_length = 20,
        required=False,
        widget=forms.TextInput(
            attrs={
            'class':'form-control ',
            'id':'name',
            'placeholder':u"输入需要筛选的老师名字"}), )

class ScheduleForm(ScheduleBaseForm):
    college_choices = (('-1', '学院'), ('0', '计算机'), ('1', '管经'))
    college = forms.ChoiceField(choices = college_choices,
        widget=forms.Select(attrs={'class':'form-control col-lg-3',}),)
    



