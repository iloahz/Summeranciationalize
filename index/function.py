from models import *
import random
from Summeranciationalize import settings
from url_normalize import url_normalize
import datetime


def getAccountByUsername(username):
    a = Account.objects.filter(username=username)
    if a:
        return a.get()
    else:
        return None


def verifyAccount(data):
    a = Account.objects.filter(username=data.get('u')).filter(password=data.get('p'))
    try:
        return a.get()
    except:
        return None


def getOrCreateLink(url):
    url = url_normalize(url)
    l = Link.objects.filter(url=url)
    if not l:
        l = Link(url=url)
        l.save()
    else:
        l = l.get()
    return l


def updateFavorite(account, link):
    f = Favorite.objects.filter(account=account, link=link)
    if f:
        f = f.get()
    else:
        f = Favorite(account, link)
    f.createOn = datetime.datetime.now()
    f.save()


def getLinkByAccount(account, depth=0):
    f = Favorite.objects.filter(account=account)
    r = Relation.objects.filter(account1=account, relationType=Relation.FOLLOW)
    l1 = len(f)
    l2 = len(r)
    if l1 + l2 == 0 or depth > 4:
        return getOrCreateLink('http://' + settings.DOMAIN + '/account/' + account.username)
    i = random.randint(0, l1 + l2 - 1)
    if i < l1:
        h = History.objects.filter(account=account, link=f[i].link)
        if h:
            return getLinkByAccount(account, depth + 1)
        else:
            return f[i].link
    else:
        return getLinkByAccount(r[i - l1].account2, depth + 1)


def createHistory(account, link):
    h = History(account=account, link=link)
    h.save()
    link.totalHits += 1
    link.save()
