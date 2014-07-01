# coding: UTF-8
from django import forms
from django.contrib.admin import widgets

class TeacherDispatchForm(forms.Form):
    password = forms.CharField(max_length=20, required=False,
                                           widget=forms.TextInput(attrs={'class':'form-control','id':"student_password",'placeholder':u"默认密码：邮箱名字",'id':'password'}
                                                                      ),
                                                                      )
    email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'class':'form-control','id':"mailbox",'placeholder':u"邮箱",'id':'email'}
                                                                           ))
    person_firstname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','id':"person_firstname",'placeholder':u"负责人"}))
