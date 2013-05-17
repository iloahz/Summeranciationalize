# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import never_cache
from function import *


@never_cache
def indexHandler(request):
    p = request.COOKIES.get('pin', '0')
    if p == '1':
        res = render_to_response('pin.html')
        res.delete_cookie('pin')
        return res
    a = verifyAccount(request.COOKIES)
    if not a:
        a = Account.objects.get(username='all')
    para = dict()
    para['link'] = getLinkByAccount(a, a)
    createHistory(a, para['link'])
    return render_to_response('index.html', para)


def signUpHandler(request):
    a = verifyAccount(request.COOKIES)
    if a:
        return redirect('/account/%s' % a.username)
    else:
        return render_to_response('signup.html')


def signInHandler(request):
    a = verifyAccount(request.COOKIES)
    if a:
        return redirect('/account/%s' % a.username)
    else:
        return render_to_response('signin.html')


def pinHandler(request):
    res = redirect('/')
    res.set_cookie('pin', '1')
    return res