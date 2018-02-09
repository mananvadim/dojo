# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cigar_wish_list/$', views.cigar_wish_list),
    url(r'^$', views.index, name='index'),
]