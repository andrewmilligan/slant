from django.conf.urls import url

from . import views

app_name = 'dataviz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.check_for_new, name='check_for_new'),
    ]
