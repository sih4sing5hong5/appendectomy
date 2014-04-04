# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 提議連署.介面 import 提議網頁


urlpatterns = patterns('',
	url(r'^.*$', 提議網頁.as_view(), name='首頁'),
)