from django.shortcuts import render
from .models import HK_jiaoyisuo

# Create your views here.
def jinmeng(request):
    HK = HK_jiaoyisuo.objects.all()
    return render(request, 'jinmeng.html', locals())

