# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext, loader
from django.utils.decorators import method_decorator
from django.views import generic
from 提議連署.模型 import 提議
import urllib
from django.views.generic.base import View

def 全部提議資料(request):
	全部資料 = 提議.objects.order_by('流水號')[:10]
	版 = loader.get_template('提議連署/全部資料.html')
	文 = RequestContext(request, {
		'全部資料': 全部資料,
	})
	return HttpResponse(版.render(文))

class 提議網頁(View):
	版 = loader.get_template('提議連署/提議.html')
	網址 = 'http://www.uisltsc.com.tw/appendectomy/proposal.php'
	下載pdf = '下載pdf'
	上傳至7_11列印 = '上傳至7-11列印'
	def get(self, request, *args, **kwargs):
		文 = RequestContext(request, {
			'方式':[self.下載pdf, self.上傳至7_11列印]
		})
		return HttpResponse(self.版.render(文))
	def post(self, request, *args, **kwargs):
		pdf資料 = self.掠pdf()
		if request.POST['送出'] == self.下載pdf:
			回應 = HttpResponse()
			回應.write(pdf資料)
			回應['Content-Type'] = 'application/pdf'
			回應['Content-Length'] = len(pdf資料)
			return 回應
		elif request.POST['送出'] == self.上傳至7_11列印:
			return HttpResponse(request.POST['送出'])
		return self.get(request, *args, **kwargs)

	def 掠pdf(self):
		'''
		連署書 PDF 範本初稿已完成：
		提議：http://www.uisltsc.com.tw/appendectomy/proposal.php
		連署：http://www.uisltsc.com.tw/appendectomy/petition.php
		使用方式：可直接使用 <FORM> 的 ACTION 來呼叫，METHOD=POST
		細節說明：
		FORM 中 Input Item 的命名規則如下：（序號皆自 0 開始）
		姓名：Name_[序號]：Name_0,Name_1...
		身分證字號：IDNo_[序號]
		性別：Sex_[序號]
		生日：Birthday_[序號]
		職業：Occupation_[序號]
		戶籍地：RegAdd_[序號]
		QRCode 影像：QRImgPath_[序號]
		'''
		參數 = {'Name_0' : 'www', 'IDNo_0' : '123456',
			'Sex_0' : 'www', 'Birthday_0' : '123456',
			'Occupation_0' : 'www', 'RegAdd_0' : '123456',
			'QRImgPath_0' : 'www', }
# 		print(urllib.parse.urlencode(參數))
		連線 = urllib.request.urlopen(
			url = self.網址,
			data = urllib.parse.urlencode(參數).encode(encoding = 'utf_8')
		)
		資料 = 連線.read()
		連線.close()
		return 資料

class 連署網頁(提議網頁):
	版 = loader.get_template('提議連署/連署.html')
	網址 = 'http://www.uisltsc.com.tw/appendectomy/petition.php'