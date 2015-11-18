from django.conf.urls import patterns, url

urlpatterns = patterns('login.views',
    url(r'^upload/$', 'upload', name='list'),
)