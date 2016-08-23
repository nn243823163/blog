# coding:utf-8
from django.http import HttpResponse


def test1(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))