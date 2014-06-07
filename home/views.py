# coding: UTF-8
'''
Created on 2014-06-07

@author: LiuYe

Desc: home view
'''
from django.shortcuts import render

def index(request):
    context={}
    return render(request,"home/home.html",context)
