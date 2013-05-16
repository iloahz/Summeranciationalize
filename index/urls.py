from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'index.views.indexHandler'),
    url(r'^signup/', 'index.views.signUpHandler'),
    url(r'^signin/', 'index.views.signInHandler'),
    url(r'^pin/', 'index.views.pinHandler'),
)
