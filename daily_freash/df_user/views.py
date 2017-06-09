#coding=utf-8
from hashlib import sha1

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *
import user_decorator
from df_goods.models import GoodsInfo
from df_order.models import OrderInfo,DetailInfo
from django.core.paginator import Paginator

# Create your views here.


# 加载注册视图
def register(request):

    return render(request, 'df_user/register.html',{'title': "天天生鲜-注册"})


# 通过ajax验证用户名是否存在
def checkname(request):

    uname=request.GET.get('uname')
    print uname
    count = UserInfo.objects.filter(uname=uname).count()
    print count
    return JsonResponse({'count': count})


# 提交注册信息
def register_post1(request):

    dic = request.POST
    user_name = dic.get('user_name')
    pwd = dic.get('pwd')
    cpwd = dic.get('cpwd')
    email = dic.get('email')
    allow = dic.get('allow')



    #判断用户名是否存在
    if UserInfo.objects.filter(uname=user_name).count() == 0:
        # 判断两次密码是否一致
        if pwd == cpwd and len(user_name) and len(pwd) and len(cpwd) and len(email):
            # 密码加密
            s1 = sha1()
            s1.update(pwd)
            pwd_s = s1.hexdigest()

            u = UserInfo()
            u.uname = user_name
            u.upwd = pwd_s
            u.uemail = email
            u.save()
            return render(request, 'df_user/login.html',{'title': '天天生鲜-登录'})
    else:
        #如果不为0说明有用户记录了
        context = {"return": "用户已经存在"}
        return render(request, 'df_user/register.html', context)


def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'name_error': 0, 'pwd_error':0 ,'name_val': uname, 'title': '天天生鲜-登录'}
    return render(request,'df_user/login.html',context)


def login_check(request):
    dic = request.POST
    username = dic.get('username')
    pwd = dic.get('pwd')
    jizhu = dic.get('jizhu')

    list = UserInfo.objects.filter(uname=username)
    # print username ,pwd

    if len(list) == 1:
        s1 = sha1()
        s1.update(pwd)

        if s1.hexdigest() == list[0].upwd:
            url = request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)
            red.set_cookie('url', '', max_age=-1)

            if jizhu != 0:
                red.set_cookie('uname', username)
            else:
                red.set_cookie('uname', '', max_age=-1)

            request.session['uname'] = username
            request.session['user_id'] = list[0].id

            return red
        else:
            context = {'name_error': 0,
                       'pwd_error': 1,
                       'name_val': list[0].uname,
                       'pwd_val': pwd,
                       'title': '天天生鲜-登录'}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'name_error': 1,
                   'pwd_error': 0,
                   'name_val': list[0].uname,
                   'pwd_val': pwd, 'title': '天天生鲜-登录'}
        return render(request, 'df_user/login.html', context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')


@user_decorator.check_log
def user_center_info(request):
    name = request.COOKIES.get('uname','')
    user = UserInfo.objects.filter(uname=name)
    # 浏览记录
    id_list = eval(request.COOKIES.get('liulan','[]'))[::-1]
    good_list = []
    for item in id_list:
        good_list.append(GoodsInfo.objects.get(id=item))

    # context = {'title': '用户中心'}
    context = {'title': '用户中心',
               'name': name,
               'adrr': user[0].uaddr,
               'phone': user[0].uphone,
               'active': ['active', '', ''],
               'page': 1,
               'liulan':good_list}
    return render(request, 'df_user/user_center_info.html', context)


@user_decorator.check_log
def user_center_order(request,page_num):
    order_list = OrderInfo.objects.filter(ouser_id=request.session['user_id']).order_by('-oid')
    paginator = Paginator(order_list, 1)
    if not page_num:
        page_num = 1
    page_list = paginator.page(int(page_num))

    context = {'title': '用户中心',
               'active': ['', 'active', ''],
               'page': 1,
               'page_list': page_list,
               'paginator': paginator}
    return render(request, 'df_user/user_center_order.html', context)


@user_decorator.check_log
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        info = request.POST
        user.ushou = info.get('ushou', '未填写')
        user.uphone = info.get('uphone', '未填写')
        user.uaddr = info.get('uadrr', '未填写')
        user.uyoubian = info.get('uyoubian', '未填写')
        user.save()

    context = {'title': '用户中心',
               'active': ['', '', 'active'],
               'user': user,
               'page': 1}
    return render(request, 'df_user/user_center_site.html', context)











