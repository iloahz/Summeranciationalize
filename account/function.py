from index.models import *
import urllib, hashlib


def getTotalFavoriteByAccount(account):
    f = Favorite.objects.filter(account=account)
    return len(f)


def getTotalHistoryByAccount(account):
    h = History.objects.filter(account=account)
    return len(h)


def getTotalFollowingByAccount(account):
    r = Relation.objects.filter(account1=account, relationType=Relation.FOLLOW)
    return len(r)


def getTotalFollowedByAccount(account):
    r = Relation.objects.filter(account2=account, relationType=Relation.FOLLOW)
    return len(r)


def getFavoritesByAccount(account):
    f = Favorite.objects.filter(account=account).order_by('-createOn')[:16]
    return f


def getHistoryByAccount(account):
    h = History.objects.filter(account=account).order_by('-hitTime')[:16]
    return h


def getOrCreateRelation(account1, account2, relationType):
    r = Relation.objects.filter(account1=account1, account2=account2, relationType=relationType)
    if not r:
        r = Relation(account1=account1, account2=account2, relationType=relationType)
        r.save()
    else:
        r = r.get()
    return r


def checkIfRelationExist(account1, account2, relationType):
    r = Relation.objects.filter(account1=account1, account2=account2, relationType=relationType)
    return len(r) > 0


def getAvatarByEmail(email):
    size = 128
    default = 'http://www.gravatar.com/avatar?s=' + str(size)
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d': default, 's': str(size)})
    return gravatar_url