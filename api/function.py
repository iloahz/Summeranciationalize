from index.models import *
from django.core.validators import validate_email
from index.function import *
from account.function import *


def createAccount(username, email, password):
    res = dict()
    if len(username) < 6 or len(username) > 60:
        res['message'] = 'Invalid user name!'
        res['return'] = 3
        return res
    try:
        validate_email(email)
    except:
        res['message'] = 'Invalid email address!'
        res['return'] = 5
        return res
    if len(password) < 1 or len(password) > 60:
        res['message'] = 'Invalid password!'
        res['return'] = 4
        return res
    a = Account.objects.filter(username=username)
    if a:
        res['message'] = 'User name already exists!'
        res['return'] = 1
        return res
    a = Account.objects.filter(email=email)
    if a:
        res['message'] = 'Email address already exists!'
        res['return'] = 2
        return res
    a = Account(username=username, email=email, password=password)
    a.save()
    # getOrCreateRelation(Account.objects.get(username='all'), a, Relation.FOLLOW)
    res['message'] = 'Account created successfully!'
    res['return'] = 0
    return res


def addFavorite(account, link):
    f = Favorite.objects.filter(account=account, link=link)
    if f:
        f = f[0]
    else:
        f = Favorite(account=account, link=link)
    f.createOn = datetime.datetime.now()
    f.save()


def delFavorite(favorite):
    favorite.delete()
    try:
        l = favorite.link
        left = Favorite.objects.filter(link=l)
        if len(left) == 0:
            l.delete()
    except:
        pass