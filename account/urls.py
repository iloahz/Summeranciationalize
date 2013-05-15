from django.conf.urls import patterns, include, url

urlpatterns = patterns('account',
    url(r'^(?P<username>\w+)$', 'views.accountHandler'),
)
