# coding: UTF-8
'''
Created on 2014-06-07

Desc: adminStaff' view, includes home(manage), review report view
'''
from django.shortcuts import render
from adminStaff.forms import NewsForm
def homeView(request):

    context={}
    return render(request,"adminStaff/home.html",context)
def newsRelease(request):
    context={}
    context.update({"newsform":NewsForm})
    return render(request,"adminStaff/news_release.html",context)

