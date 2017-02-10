from django.shortcuts import render
#render是渲染模板

# Create your views here.
from django.http import HttpResponse

def add(request):
	a = request.GET['a']
	#request.GET 类似于一个字典，
	#更好的办法是用 request.GET.get('a', 0) 
	#当没有传递 a 的时候默认 a 为 0
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def index(request):
	string = u"我在自强学堂学习Djan\n"
	#在视图中传递了一个字符串名称是 string 到模板 home.html
	#home.html:  {{ string }}
	TutorialList = ["HTML","CSS","jQuery","Python","Django"]
	info_dict = {'site':u'自强学堂','content':u'各种IT技术教程'}
	List = map(str,range(100))
	#一个长度为100的List
	#return render(request,'home.html',{'string':string})
	#return render(request,'home.html',{'TutorialList':TutorialList})
	#return render(request,'home.html',{'info_dict':info_dict})
	return render(request,'home.html',{'List':List})

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#用户收藏夹中收藏的URL是旧的，让以前的 /add/3/4/自动跳转到现在新的网址
#如用户收藏夹中有 /add/4/5/ ，访问时就会自动跳转到新的 /new_add/4/5/ 
def old_add2_redirect(request,a,b):
	return HttpResponseRedirect(
		reverse( 'add2', args = (a,b) )
		)