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
def show(request):
    context={}
    return render(request,"home/show.html",context)
def showProject(request, project_id = ""):
    context={}
    return render(request,"home/show_project.html",context)
def newsListByCate(request, news_cate):
    context={}
    context["news_cate"] = news_cate
    context['%s_active' % news_cate] = 'active'
    return render(request, 'home/newsContentByCate.html', \
                  context)
