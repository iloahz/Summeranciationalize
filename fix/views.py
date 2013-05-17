# Create your views here.

from django.http import HttpResponse
from index.models import *
from datetime import datetime


def t20130517(request):
    f = Favorite.objects.all()
    for i in f:
        if not i.createOn:
            i.createOn = datetime.now()
            i.save()
    return HttpResponse('fixed')