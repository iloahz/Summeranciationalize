# Create your views here.

from django.shortcuts import render_to_response, redirect
from index.models import *
from index.function import *
from function import *


def defaultHandler(request):
    return redirect('/signup')


def accountHandler(request, username):
    a = Account.objects.filter(username=username)
    if a:
        a = a.get()
        para = dict()
        para['username'] = username
        para['totalFavorite'] = getTotalFavoriteByAccount(a)
        para['favorites'] = getFavoritesByAccount(a)
        para['history'] = getHistoryByAccount(a)
        para['avatar'] = getAvatarByEmail(a.email)
        para['since'] = a.createdOn.strftime('%Y.%m.%d')
        para['totalHits'] = getTotalHistoryByAccount(a)
        para['following'] = checkIfRelationExist(getAccountByUsername(request.COOKIES.get('u')), getAccountByUsername(username), Relation.FOLLOW)
        para['self'] = a.username == request.COOKIES.get('u')
        return render_to_response('account_overview.html', para)
    else:
        return defaultHandler(request)