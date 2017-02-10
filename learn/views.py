from django.shortcuts import render

# Create your views here.

#coding:utf-8
#定义视图函数（访问页面时的内容）

from django.http import HttpResponse
#用来向网页返回内容的，就像Python中的 print 一样，
#只不过 HttpResponse 是把内容显示到网页上
def index(request):
#定义一个index()函数，第一个参数必须是 request，
#与网页发来的请求有关，
#request 变量里面包含get或post的内容，
#用户浏览器，系统等信息在里面
	return HttpResponse(u"欢迎光临 自强学堂！")
	#函数返回了一个 HttpResponse 对象，
	#可以经过一些处理，最终显示几个字到网页上
