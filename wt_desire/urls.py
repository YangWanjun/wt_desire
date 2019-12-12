"""wt_desire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve

from desire.views import IndexView, WallView, DesireImageView

urlpatterns = [
    path('desire/admin/', admin.site.urls),
    url(r'^desire/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^desire$', IndexView.as_view(), name='index'),
    url(r'^desire/slider$', WallView.as_view(), {'type': 'slider'}, name='slider'),
    url(r'^desire/tree', WallView.as_view(), {'type': 'tree'}, name='tree'),
    url(r'^desire/bubble', WallView.as_view(), {'type': 'bubble'}, name='bubble'),
    url(r'^desire/email/(?P<email>[^/]+)$', DesireImageView.as_view(),),
]
