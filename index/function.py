from models import *
import random
from Summeranciationalize import settings


def getAccountByUsername(username):
    a = Account.objects.filter(username=username)
    if a:
        return a.get()
    else:
        return None


def verifyAccount(username, password):
    a = Account.objects.filter(username=username).filter(password=password)
    try:
        return a[0]
    except:
        return None


def getOrCreateLink(url):
    l = Link.objects.filter(url=url)
    if not l:
        l = Link(url=url)
        l.save()
    else:
        l = l.get()
    return l


def getLinkByAccount(account):
    f = Favorite.objects.filter(account=account)
    r = Relation.objects.filter(account1=account).filter(relationType=1)
    l1 = len(f)
    l2 = len(r)
    if l1 + l2 == 0:
        return getOrCreateLink('http://' + settings.DOMAIN + '/account/' + account.username)
    i = random.randint(0, l1 + l2 - 1)
    if i < l1:
        return f[i].link
    else:
        return getLinkByAccount(r[i - l1].account2)


def createHistory(account, link):
    h = History(account=account, link=link)
    h.save()
    link.totalHits += 1
    link.save()
