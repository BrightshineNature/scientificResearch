# coding: UTF-8
'''
Created on 2014-06-07

Desc: expert' view, includes home(manage), review report view
'''
from django.shortcuts import render

def home_view(request):
    context={}
    return render(request,"expert/home.html",context)
