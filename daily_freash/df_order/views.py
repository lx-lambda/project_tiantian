# coding=utf-8
from django.shortcuts import render
from df_user.models import UserInfo
from df_cart.models import MyCart

# Create your views here.


# 加载首页视图,
def order(request):
    user = UserInfo.objects.get(id=request.session['user_id'])

    carts = request.GET.getlist('cart_id')
    order_list = MyCart.objects.filter(id__in=carts)

    context = {'title': "我的订单",
               'active': ['', 'active', ''],
               'page': 1,
               'user': user,
               'order_list': order_list}
    return render(request, 'df_order/order.html', context)

