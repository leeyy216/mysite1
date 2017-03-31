"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#定义视图函数相关的URL(网址) ，即规定 访问什么网址对应什么内容）
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views	#new
from calc import views as calc_views	#new1
from learn1 import views as learn1_views    #new0208

from boot import views as boot_views    #new20170330

from django.conf import settings    #0330
from django.conf.urls.static import static


#Django 查找模板的过程是在每个 app 的 templates 文件夹中找
#（而不只是当前 app 中的代码只在当前的 app 的 templates 文件夹中找）

urlpatterns = [
    #url(r'^$',learn_views.index),	#new
    url(r'^$',calc_views.index, name = 'home'), #new
    
    url(r'^add/$',calc_views.add, name = 'add'),	#new1
    
    #url(r'^add/(\d+)/(\d+)/$',calc_views.add2, name = 'add2'),	#new2
    #将收藏夹中的旧url：add/4/5重定向到新的url：newadd/4/5
    url(r'^add/(\d+)/(\d+)/$',calc_views.old_add2_redirect),    #new0210
    url(r'^newadd111/(\d+)/(\d+)/$', calc_views.add2, name = 'add2'),  #new0210
    
    url(r'^home1/$', learn1_views.home1, name='home1'),    #new0208
    
    url(r'^admin/', admin.site.urls),
    url(r'^boot/',boot_views.bootindex,name='bootindex'),   #0330

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

[]