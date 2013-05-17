from django.conf.urls import patterns, include, url

urlpatterns = patterns('fix',
    url(r'^20130517$', 'views.t20130517'),
)
