# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import never_cache
from function import *


@never_cache
def indexHandler(request):
    a = verifyAccount(request)
    if not a:
        a = Account.objects.get(username='all')
    para = dict()
    para['link'] = getLinkByAccount(a)
    createHistory(a, para['link'])
    return render_to_response('index.html', para)


def signUpHandler(request):
    a = verifyAccount(request)
    if a:
        return redirect('/account/%s' % a.username)
    else:
        return render_to_response('signup.html')


def signInHandler(request):
    a = verifyAccount(request)
    if a:
        return redirect('/account/%s' % a.username)
    else:
        return render_to_response('signin.html')