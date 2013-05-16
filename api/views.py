# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect
import json
import index.views
from function import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def defaultHandler(request):
    return index.views.indexHandler(request)


@csrf_exempt
def signUpHandler(request):
    try:
        u = request.POST.get('u')
        e = request.POST.get('e')
        p = request.POST.get('p')
        res = createAccount(u, e, p)
        return HttpResponse(json.dumps(res), content_type='application/json')
    except:
        return defaultHandler(request)


@csrf_exempt
def signInHandler(request):
    try:
        a = verifyAccount(request.POST)
        res = dict()
        if a:
            res['message'] = 'Signed in successfully!'
            res['return'] = 0
        else:
            res['message'] = 'Invalid user name or password!'
            res['return'] = 1
        return HttpResponse(json.dumps(res), content_type='application/json')
    except:
        return defaultHandler(request)


@csrf_exempt
def favoriteHandler(request, cmd):
    a = verifyAccount(request.POST)
    if not a:
        return defaultHandler(request)
    if cmd == 'add':
        l = getOrCreateLink(request.POST.get('url'))
        f, c = Favorite.objects.get_or_create(account=a, link=l)
        res = dict()
        res['message'] = 'Favorite added successfully!'
        res['return'] = 0
        return HttpResponse(json.dumps(res), content_type='application/json')
    elif cmd == 'del':
        l = getOrCreateLink(request.POST.get('url'))
        f = Favorite.objects.filter(account=a).filter(link=l).get()
        f.delete()
        res = dict()
        res['message'] = 'Favorite deleted successfully!'
        res['return'] = 0
        return HttpResponse(json.dumps(res), content_type='application/json')
    else:
        return defaultHandler(request)


@csrf_exempt
def relationHandler(request, cmd):
    a = verifyAccount(request.POST)
    if not a:
        return defaultHandler(request)
    if cmd == 'follow':
        b = Account.objects.get(username=request.POST.get('target'))
        r = getOrCreateRelation(a, b, Relation.FOLLOW)
        res = dict()
        res['message'] = 'Followed successfully!'
        res['return'] = 0
        return HttpResponse(json.dumps(res), content_type='application/json')
    elif cmd == 'unfollow':
        b = Account.objects.get(username=request.POST.get('target'))
        r = getOrCreateRelation(a, b, Relation.FOLLOW)
        if r:
            r.delete()
        res = dict()
        res['message'] = 'Unfollowed successfully!'
        res['return'] = 0
        return HttpResponse(json.dumps(res), content_type='application/json')
    else:
        return defaultHandler(request)