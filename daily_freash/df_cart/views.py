# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from df_goods.models import GoodsInfo
from df_user.models import UserInfo
from models import MyCart
from df_user.user_decorator import check_log

# Create your views here.

@check_log
def cart(request):
    print request.get_full_path()
    good_list = MyCart.objects.filter(cuser_id=int(request.session.get('user_id')))
    context = {'title': "购物车",
               'page': 1,
               'good_list': good_list}
    return render(request, 'df_cart/cart.html', context)


@check_log
def add(request, good_id, count, source):
    # 根据商品找记录,若能找到商品记录和相对因的记录说明有记录
    carts = MyCart.objects.filter(cgood_id=int(good_id)).filter(cuser_id=int(request.session.get('user_id')))
    if len(carts) == 0:
        cart = MyCart()
        cart.cuser_id = request.session.get('user_id')
        cart.cgood_id = int(good_id)
        cart.ccount = int(count)
        cart.save()
    else:
        if source == '0':
            carts[0].ccount = count
            carts[0].save()

        else:

            carts[0].ccount += int(count)
            carts[0].save()

    data = MyCart.objects.filter(cuser_id=int(request.session.get('user_id'))).count()

    print data
    if request.is_ajax():
        return JsonResponse({'data': data})

    else:
        return HttpResponseRedirect('/cart/')



