from django.shortcuts import render
from django.utils import simplejson
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from django.template import Context
from django.http import HttpResponse, Http404

from const import *
from adminStaff.models import News,ProjectSingle
from backend.utility import getContext
from backend.logging import loginfo


@dajaxice_register
def getNewsListPagination(request,page,news_cate):
    message=""
    page =int(page)
    loginfo(news_cate)
    try:
        if news_cate == NEWS_CATEGORY_DOCUMENTS:
            news_list = News.objects.exclude(news_document=u'').order_by('-news_date')
        else:
            news_list = News.objects.filter(news_category__category=news_cate).order_by('-news_date')
    except:
        raise Http404
    context = getContext(news_list,page, 'item')
    html = render_to_string("widgets/news/_newsList.html",context)
    return simplejson.dumps({"message":message,"html":html})
