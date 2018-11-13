from django.conf.urls import include, url
import HelloDjangoApp.views
import HelloDjangoApp.api.views

urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^messages$', HelloDjangoApp.api.views.ListAPIView.as_view(), name='messages'),
    url(r'^messages/update/(?P<pk>[0-9]+)$', HelloDjangoApp.api.views.UpdateAPIView.as_view(), name='update')
]