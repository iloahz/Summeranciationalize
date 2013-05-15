# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from function import *


def indexHandler(request):
    a = verifyAccount(request.COOKIES.get('u'), request.COOKIES.get('p'))
    if not a:
        a = Account.objects.get(username='all')
    para = dict()
    para['link'] = getLinkByAccount(a)
    createHistory(a, para['link'])
    return render_to_response('index.html', para)


def signUpHandler(request):
    return render_to_response('signup.html')


def signInHandler(request):
    return render_to_response('signin.html')