# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from df_user.models import UserInfo
from df_cart.models import MyCart
from models import *
from django.db import transaction
from datetime import datetime

# Create your views here.
'''
1、判断库存
2、减少库存
3、创建订单对象
4、创建详单对象
5、删除购物车
对于以上操作，应该使用事务
问题是：在django的模型类中如何使用事务？

未实现功能：
    真实支付
    物流跟踪
'''


# 提交订单信息
@transaction.atomic
def order_commit(request):

    user_id = request.session.get('user_id')
    # print user_id
    post = request.POST
    cart_ids = post.getlist('cart_id')
    address = post.get('address')
    # 创建初始节点对对象
    s_point = transaction.savepoint()
    try:
        # 创建订单对象
        now = datetime.now()
        order = OrderInfo()
        order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'), user_id)
        order.ouser_id = user_id
        order.oaddr = address
        order.odata = now
        order.ototal = 0
        order.save()
        total = 0

        for cart_id in cart_ids:
            cart = MyCart.objects.get(id=cart_id)
            if cart.cgood.gkucun >= cart.ccount:
                # 创建详单对象

                detail_info = DetailInfo()
                detail_info.ogood = cart.cgood
                detail_info.order = order
                detail_info.oprice = cart.cgood.gprice
                detail_info.ocount = cart.ccount
                detail_info.save()

                cart.cgood.gkucun -= cart.ccount
                # 注意这里不是 cart.save() 是要通过cart找到good对象,然后与改变
                cart.cgood.save()
                cart.delete()

                total += cart.cgood.gprice*cart.ccount

            else:
                transaction.savepoint_rollback(s_point)
                return HttpResponse(cart.ccount)
                # return redirect('/order/')
        order.ototal = total
        order.save()

        transaction.savepoint_commit(s_point)

        # return HttpResponse(cart.ccount)
        return redirect('/user_center_order/')

    except Exception as e:
        transaction.savepoint_rollback(s_point)
        return redirect('/order/')
        print e

def pay(request, order_id):

    order = OrderInfo.objects.get(oid=order_id)
    order.oispay = True
    order.save()
    return redirect('/order/')

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

