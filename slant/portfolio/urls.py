from django.conf.urls import url

from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[a-zA-Z0-9-_]+)/$', views.detail, name='detail'),
    ]
