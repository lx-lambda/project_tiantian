#coding=utf-8
from django.http import HttpResponseRedirect


def check_log(fun):

    def check_log_fun(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return fun(request,*args, **kwargs)
        else:

            red = HttpResponseRedirect('/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return check_log_fun