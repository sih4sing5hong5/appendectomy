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

def 首頁(request):
	全部資料 = 提議.objects.order_by('流水號')[:10]
	版 = loader.get_template('提議連署/全部資料.html')
	文 = RequestContext(request, {
		'全部資料': 全部資料,
	})
	return HttpResponse(版.render(文))