# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render

def homeView(request):

    context={}
    return render(request,"finance/home.html",context)
