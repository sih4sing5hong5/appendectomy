# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 提議連署.介面 import 提議網頁
from 提議連署.介面 import QRCode


urlpatterns = patterns('',
	url(r'^QRCode/(?P<資料>.*)$', QRCode, name='QRCode'),
	url(r'^.*$', 提議網頁.as_view(), name='首頁'),
)