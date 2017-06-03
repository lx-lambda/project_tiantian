# coding=utf-8
from django.shortcuts import render

# Create your views here.


def cart(request):
    context = {'title': "我的购物车",
               'page': 1}
    return render(request, 'df_cart/cart.html', context)