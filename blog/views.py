from django.shortcuts import render
import logging
from django.conf import settings

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

    return render(request,'index.html',locals())

def love(request):

    # try:
    #     file = open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)

    return render(request,'love.html',locals())