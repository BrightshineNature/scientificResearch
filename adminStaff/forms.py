# coding: UTF-8
from datetime import *
from django import  forms
from backend.logging import loginfo
from django.forms import ModelForm
from django.contrib.admin import widgets
from const.models import NewsCategory
from adminStaff.models import TemplateNoticeMessage,News
from users.models import College
from const import COLLEGE_USER
class NewsForm(ModelForm):
    class Meta:
        model = News
        widgets = {"news_title": forms.TextInput(attrs={'class':'form-control','id':"news_title",'placeholder':u"新闻标题"}),
                   "news_content": forms.Select(attrs={'class':'form-control'}),
                   "news_date": forms.DateInput(attrs={'class':'form-control'}),
                   "news_category":forms.Select(attrs={"class":'form-control'}),
                   "news_document": forms.FileInput(attrs={'class':'form-control'}),
                  }
        news_cate_list = NewsCategory.objects.all()
        choice_list = []
        for obj in news_cate_list:
            choice_list.append((obj.id, obj.get_category_display()))

class DispatchForm(forms.Form):
    username = forms.CharField(max_length=20, required=True,
                                           widget=forms.TextInput(attrs={'class':'form-control','id':"username",'placeholder':u"用户名",'id':'username'}))
    password = forms.CharField(max_length=20, required=False,
                                           widget=forms.TextInput(attrs={'class':'form-control','id':"password",'placeholder':u"默认密码：用户名",'id':'password'}))
    email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'class':'form-control','id':"mailbox",'placeholder':u"邮箱",'id':'email'}))
    person_firstname = forms.CharField(required=True,
                                       widget=forms.TextInput(attrs={'class':'form-control','id':"person_firstname",'placeholder':u"负责人"}))

class DispatchAddCollegeForm(DispatchForm):
    college = forms.ChoiceField(required=True,choices =(),widget=forms.Select(attrs={'class':'form-control'}))
    def __init__(self,*args,**kwargs):
        user = kwargs.get("user",None)
        if user != None:
            del kwargs['user']
        super(DispatchAddCollegeForm, self).__init__(*args, **kwargs)
        if user != None:
            self.fields["college"].choices = [(obj.id,obj.name) for obj in College.objects.filter(college_user__userid= user)]
        else:
            self.fields["college"].choices = [(obj.id,obj.name) for obj in College.objects.all()]
class ObjectForm(forms.Form):
    name = forms.CharField(
      label='Your name',
      max_length=200, required=True,
      widget=forms.TextInput(attrs={'class':'form-control object_name','placeholder':u""}),)

class TemplateNoticeMessageForm(ModelForm):
    class Meta:
        model=TemplateNoticeMessage
        fields=('title','message')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control','row':10}),
        }
