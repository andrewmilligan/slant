"""slant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve as dj_static_serve

import dataviz.views as dv

urlpatterns = [
    url(r'^$', dv.index),
    #url(r'^admin/', admin.site.urls),
    url(r'^dataviz/', include('dataviz.urls')),
    url(r'^feed/', include('feed.urls')),
    #url(r'^news/', include('stories.urls')),
    url(r'^comics/', include('comics.urls')),
    url(r'^static/(?P<path>.*)$', dj_static_serve,
      {'document_root': settings.STATIC_ROOT}),
    url(r'^', include('general.urls')),
]
