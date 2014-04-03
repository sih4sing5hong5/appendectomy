# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 提議連署.介面 import 首頁


urlpatterns = patterns('',
	url(r'^.*$', 首頁, name='首頁'),
)