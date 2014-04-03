# -*- coding: utf-8 -*-
from django.db import models

__產生種類陣列 = lambda 種類:[(物件, 物件) for 物件 in 種類]
印出 = '印出'
收到 = '收到'
作廢 = '作廢'  # 因為重印
未送件 = '未送件'
送去中選會 = '送去中選會'
狀況種類 = __產生種類陣列([印出, 收到, 作廢, 未送件, 送去中選會, ])

class 提議(models.Model):
	流水號 = models.AutoField(primary_key=True)
	信箱 = models.EmailField()
	狀況 = models.CharField(max_length=20, choices=狀況種類, default=印出)
	收錄時間 = models.DateTimeField(auto_now_add=True)
	修改時間 = models.DateTimeField(auto_now=True)

class 連署(models.Model):
	流水號 = models.AutoField(primary_key=True)
	信箱 = models.EmailField()
	狀況 = models.CharField(max_length=20, choices=狀況種類, default=印出)
	收錄時間 = models.DateTimeField(auto_now_add=True)
	修改時間 = models.DateTimeField(auto_now=True)
