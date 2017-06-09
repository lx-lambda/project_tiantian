# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# Create your views here.


# 加载首页视图,
def index(request):
    typeinfo_list = TypeInfo.objects.all()
    list = []
    for typeinfo in typeinfo_list:
        list.append({
            'type': typeinfo,
            'newlist': typeinfo.goodsinfo_set.order_by('-id')[0:4],
            'clicklist': typeinfo.goodsinfo_set.order_by('-gclick')[0:3],
        })

    context = {'title': "首页",
               'page': 0,
               'list': list}
    return render(request, 'df_goods/index.html', context)


def detail(request, tid):
    good = GoodsInfo.objects.get(id=tid)
    t1_new = GoodsInfo.objects.filter(gtype_id=good.gtype.id).order_by("-id")[0:2]
    good.gclick += 1
    good.save()

    # 浏览记录
    read_list = []
    liu_lan = request.COOKIES.get('liulan', '')
    if liu_lan == '':
        read_list.append(tid)
    else:
        read_list = eval(liu_lan)

        if tid in read_list:
            read_list.remove(tid)

        read_list.append(tid)
        read_list = read_list[-5:]

    read_list = str(read_list)

    context = {'title': '商品详情',
               'page': 0,
               'good': good,
               't1_new': t1_new}

    red = render(request, 'df_goods/detail.html', context)
    red.set_cookie('liulan', read_list)
    return red


def list(request, tid, page_num, sort):
    # print tid
    # print page_num
    # print sort
    if sort == '1':  # 按最新 默认
        goodslist = GoodsInfo.objects.filter(gtype_id=tid).order_by("-id")
    elif sort == '2':  # 按价格排序
        goodslist = GoodsInfo.objects.filter(gtype_id=tid).order_by("-gprice")
    elif sort == '3':  # 按点击量排序
        goodslist = GoodsInfo.objects.filter(gtype_id=tid).order_by("-gclick")

    t1_new = GoodsInfo.objects.filter(gtype_id=tid).order_by("-id")[0:2]  # 取最新的两个(新品展示用)
    typeinfo = TypeInfo.objects.get(id=tid)  # 获取相应的品了类
    paginator = Paginator(goodslist, 10)
    page_list = paginator.page(int(page_num))

    print typeinfo.id


    context = {'title': '商品列表',
               'title1': '1',
               'page': 0,
               't1_new': t1_new,
               'page_list': page_list,
               'paginator': paginator,
               'typeinfo': typeinfo,
               'sort': int(sort)}
    return render(request, 'df_goods/list.html', context)