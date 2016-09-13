#coding:utf-8
from django.shortcuts import render
import logging
from django.conf import settings
from .models import Article



logger = logging.getLogger('blog.views')

def global_settings(request):
    return {
        'SITE_NAME':settings.SITE_NAME,
        'SITE_DESC':settings.SITE_DESC,
        'STATIC_URL':settings.STATIC_URL
    }

# Create your views here.
def index(request):
    # try:
    #     file = open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)
    articles_index = Article.objects.all()
    return render(request,'index.html',locals())

def love(request):
    # try:
    #     file = open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)
    return render(request,'love.html',locals())

def test1(request):
    # try:
    #     file = open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)
    return render(request,'blog/test1.html',locals())

def article(request,id):
    # Article_query = Article.objects.values('content')
    # article_list = list()
    # for article_query in Article_query:
    #     article_query = article_query['content']
    #     article_list.append(article_query)
    article_html = Article.objects.filter(id = id)
    return render(request,'blog/article.html',locals())



