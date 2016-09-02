#coding:utf-8
from django.shortcuts import render
from .models import Photo
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# Create your views here.

def caoliu(request):

    ####直接返回图片#####
    # photos = Photo.objects.values('link')[00:100]
    # link = []
    # for photo in photos:
    #     photo = photo['link']
    #     print photo
    #     link.append(photo)
    # return render(request,'caoliu.html',locals())

    #####返回标题########
    photo_titles = Photo.objects.values('title').distinct()
    paginator = Paginator(photo_titles , 50)

    try:
        page = int(request.GET.get('page',1))
        photo_titles = paginator.page(page)
    except (InvalidPage,EmptyPage,PageNotAnInteger):
        photo_titles = paginator.page(1)
    titles = []
    for photo_title in photo_titles:
        photo_title = photo_title['title']
        titles.append(photo_title)

    # photos =    Photo.objects.all()
    # paginator = Paginator(photos,50)
    # try:
    #     page = int(request.GET.get('page',1))
    #     photos = paginator.page(page)
    # except (InvalidPage,EmptyPage,PageNotAnInteger):
    #     photos = paginator.page(1)

    return render(request, 'caoliu.html', locals())

def list(request):
    get_title = request.GET['title']
    get_photos = Photo.objects.values('link').filter(title=get_title)
    get_urls = Photo.objects.values('url').filter(title=get_title)
    get_links = []
    get_url = ''
    for get_photo in get_photos:
        get_photo = get_photo['link']
        get_links.append(get_photo)
    for url in get_urls:
        get_url = url['url']
    return render(request, 'list.html', locals())

