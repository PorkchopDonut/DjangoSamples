from django.conf.urls import include, url
import HelloDjangoApp.views

urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^all$', HelloDjangoApp.views.index, name='all'),
    url(r'^unread$', HelloDjangoApp.views.unread, name='unread'),
    url(r'^update$', HelloDjangoApp.views.update, name='update')
]