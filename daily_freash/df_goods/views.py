# coding=utf-8
from django.shortcuts import render

# Create your views here.


# 加载首页视图,
def index(request):
    context = {'title': "首页",
               'page': 0}
    return render(request, 'df_goods/index.html', context)
