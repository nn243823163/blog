"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from quickstart.views import UserViewSet,GroupViewSet,ArticleViewSet
from blog.views import index
from blog.views import love,test1 as blogtest,article
from .views import test1,add,add2
from photo.views import caoliu,list
from django.conf import settings
from testapp.views import test_upload


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'article_api',ArticleViewSet)
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index,name='index'),
    url(r'^love/', love,name='love'),
    url(r'^test/', test1,name='test'),
    url(r'^add/$', add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', add2, name='add2'),
    url(r'^article/$',article,name='article'),
    url(r'^test3/$', blogtest, name='test2'),
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^caoliu', caoliu, name='caoliu'),
    url(r'^list/$', list, name='list'),
    url(r"^uploads/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT,}),
    url(r'^testapp/', include('testapp.urls')),

]
