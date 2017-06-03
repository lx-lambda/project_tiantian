# coding=utf-8
from django.shortcuts import render
from df_user.models import *

# Create your views here.


# 加载首页视图,
def order(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    context = {'title': "我的订单",
               'active': ['', 'active', ''],
               'page': 1,
               'user': user}
    return render(request, 'df_order/order.html', context)
