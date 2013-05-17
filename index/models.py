from django.db import models
from django.db.models import Q

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s' % (self.username, self.email)


class Link(models.Model):
    url = models.CharField(max_length=4096)
    totalHits = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s - %d' % (self.url, self.totalHits)


class Favorite(models.Model):
    account = models.ForeignKey(Account)
    link = models.ForeignKey(Link)
    createOn = models.DateTimeField()

    def __unicode__(self):
        return '%s - %s - %s' % (self.account.username, self.link.url, self.createOn)


class History(models.Model):
    account = models.ForeignKey(Account)
    link = models.ForeignKey(Link)
    hitTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s - %s' % (self.account.username, self.link.url, self.hitTime)


class Relation(models.Model):
    FOLLOW = 1
    account1 = models.ForeignKey(Account, related_name='account1')
    account2 = models.ForeignKey(Account, related_name='account2')
    relationType = models.IntegerField()

    def __unicode__(self):
        return '%s - %s - %d' % (self.account1.username, self.account2.username, self.relationType)