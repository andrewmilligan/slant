from django.conf.urls import url

from . import views

app_name = 'comics'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^last/$', views.check_for_new, name='check_for_new'),
    ]
