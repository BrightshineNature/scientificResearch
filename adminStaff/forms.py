# coding: UTF-8
from datetime import *
from django import  forms
#from const import NEWS_MAX_LENGTH
#from const.models import NewsCategory
from django.contrib.admin import widgets
from adminStaff.models import TemplateNoticeMessage
class NewsForm(forms.Form):
    NEWS_MAX_LENGTH=500
    news_title = forms.CharField(max_length=200, required=True,
                                 widget=forms.TextInput(attrs={'class':'form-control','id':"news_title",'placeholder':u"新闻标题"}),)
    news_content = forms.CharField(max_length=NEWS_MAX_LENGTH, required=True)
    news_date = forms.DateField(required=True,widget=forms.DateInput(attrs={'class':'form-control'}))
    news_document = forms.FileField(label='select', help_text='文件上传', required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    #news_cate_list = NewsCategory.objects.all()
    #choice_list = []
    #for obj in news_cate_list:
        #choice_list.append((obj.id, obj.get_category_display()))
    #news_category = forms.ChoiceField(choices=choice_list)
class SchoolDispatchForm(forms.Form):
    password = forms.CharField(max_length=20, required=False,
                                           widget=forms.TextInput(attrs={'class':'form-control','id':"student_password",'placeholder':u"默认密码：邮箱名字",'id':'password'}
                                                                      ),
                                                                      )
    email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'class':'form-control','id':"mailbox",'placeholder':u"邮箱",'id':'email'}
                                                                           ))
    person_firstname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','id':"person_firstname",'placeholder':u"负责人"}))

class SpecialForm(forms.Form):
    name = forms.CharField(max_length=200, required=True,
                                 widget=forms.TextInput(attrs={'class':'form-control','id':"special",'placeholder':u""}),)

class CollegeForm(forms.Form):
    name = forms.CharField(max_length=200, required=True,
                                 widget=forms.TextInput(attrs={'class':'form-control','id':"college",'placeholder':u""}),)    
class CollegeDispatchForm(forms.Form):
    COLLEGE_LIST = ((0, "college0"), (1, "college1"), )
    password = forms.CharField(max_length=20, required=False,
                                           widget=forms.TextInput(attrs={'class':'form-control','id':"student_password",'placeholder':u"默认密码：邮箱名字",'id':'password'}
                                                                      ),
                                                                      )
    email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'class':'form-control','id':"mailbox",'placeholder':u"邮箱",'id':'email'}
                                                                           ))
    college = forms.ChoiceField(required=True,choices=COLLEGE_LIST,widget=forms.Select(attrs={'class':'form-control'}))
    person_firstname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','id':"person_firstname",'placeholder':u"负责人"}))

class ExpertDispatchForm(forms.Form):
    password = forms.CharField(max_length=20, required=False,
                                           widget=forms.TextInput(attrs={'class':'form-control','id':"student_password",'placeholder':u"默认密码：邮箱名字",'id':'password'}
                                                                      ),
                                                                      )
    email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'class':'form-control','id':"mailbox",'placeholder':u"邮箱",'id':'email'}
                                                                           ))
    person_firstname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','id':"person_firstname",'placeholder':u"负责人"}))
class TemplateNoticeMessageForm(forms.Form):
    class Meta:
        model=TemplateNoticeMessage
        fields=('title','message')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control','row':10}),
        }
        
