from django.conf.urls import patterns, include, url

urlpatterns = patterns('api',
    url(r'^signup$', 'views.signUpHandler'),
    url(r'^signin$', 'views.signInHandler'),
    url(r'^favorite/(?P<cmd>\w+)', 'views.favoriteHandler'),
    url(r'^relation/(?P<cmd>\w+)', 'views.relationHandler'),
)
