from django.shortcuts import render
from .models import HK_jiaoyisuo

# Create your views here.
def jinmeng(request):
    HK = HK_jiaoyisuo.objects.all()

    # time_hk = HK_jiaoyisuo.objects.values('time_hk')[0:10]
    # time_hk_html = list()
    # for i in time_hk:
    #     time_hk_html.append(str(i['time_hk'].strftime(' %H:%M')))
    #
    # data1 = HK_jiaoyisuo.objects.values('data1')[0:10]
    # data1_html = list()
    # for i in data1:
    #     data1_html.append(int(str(i['data1'])))
    #
    # data2 = HK_jiaoyisuo.objects.values('data2')[0:10]
    # data2_html = list()
    # for i in data2:
    #     data1_html.append(int(str(i['data2'])))

    return render(request, 'jinmeng.html', locals())

