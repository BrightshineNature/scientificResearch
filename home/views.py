# coding: UTF-8
'''
Created on 2014-06-07

@author: LiuYe

Desc: home view
'''
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, Http404
from const import *
from adminStaff.models import News,ProjectSingle,HomePagePic
from common.forms import ScheduleBaseForm
from backend.utility import getContext
from settings import STATIC_URL, MEDIA_URL
from backend.logging import loginfo
from common.views import schedule_form_data
def index(request):
    news_announcement = News.objects.filter(news_category__category=NEWS_CATEGORY_ANNOUNCEMENT).order_by('-news_date')
    news_docs = News.objects.exclude(news_document=u'').order_by('-news_date')
    context = getContext(news_announcement, 1, "news_announcement",page_elems=7)
    context.update(getContext(news_docs,1,"news_docs",page_elems = 7))
    def convert_url(raw_url):
        return MEDIA_URL + raw_url[raw_url.find(MEDIA_URL)+len(MEDIA_URL):]
    homepage_pic = HomePagePic.objects.all()
    flag = True
    for pic in homepage_pic:
        pic.url = convert_url(pic.pic_obj.url)
        print pic.url
        if flag:
            pic.active = True
            flag = False
        else: pic.active = False
    context.update({
        'homepage_pic': homepage_pic,
    })
    return render(request,"home/home.html",context)

def show(request):
    project_page = request.GET.get('project_page')
    try:
        project_page = int(project_page)
    except:
        project_page = 1
    if project_page <= 0:
        raise Http404
    schedule_form = ScheduleBaseForm()
    if request.method == 'POST':
        schedule_form = ScheduleBaseForm(request.POST)
        pro_list=get_search_data(schedule_form)
    else:
        pro_list=ProjectSingle.objects.all()
    context = getContext(pro_list,project_page,'project',page_elems = 9)
    context.update({
               'schedule_form':schedule_form,
             })
    return render(request,"home/show.html",context)
def showProject(request, project_id = ""):
    context={}
    return render(request,"home/show_project.html",context)
def newsListByCate(request, news_cate):
    try:
        if news_cate == NEWS_CATEGORY_DOCUMENTS:
            news_list = News.objects.exclude(news_document=u'').order_by('-news_date')
        else:
            news_list = News.objects.filter(news_category__category=news_cate).order_by('-news_date')
    except:
        raise Http404
    context = getContext(news_list,1, 'item')
    context["news_cate"] = news_cate
    context['%s_active' % news_cate] = 'active'
    return render(request, 'home/newsContentByCate.html', \
                  context)
def get_news(news_id = None):
    if news_id:
        try:
            news_content = News.objects.get(id = news_id)
        except:
            raise Http404
    else: # get latest news
        news_content = (News.objects.count() and News.objects.order_by('-news_date')[0]) or None
    return news_content

def read_news(request, news_id):
    news = get_news(news_id)
    news_cate = news.news_category
    context = Context({
        'news': news,
        'news_cate':news_cate,
        '%s_active' % news_cate.category: 'active',
    })
    return render(request,'home/news-content.html',context)
