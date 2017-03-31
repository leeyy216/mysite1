from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(u'标题',max_length = 256)
	content = models.TextField(u'内容')

	pub_date = models.DateTimeField(u'发表时间', auto_now_add = True, editable = True)
	update_time = models.DateTimeField(u'更新时间', auto_now = True, null = True)

	def __str__(self):
		return self.title

#20170306-django中级-数据导入-15:43
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()

	def __str__(self):
		return self.title
#20170306-django中级-数据导入

#20170316
class Enrollinfo(models.Model):
	from_sch = models.CharField(max_length = 30)
	stu_num = models.CharField(max_length = 30)
	stu_name = models.CharField(max_length = 30)
	into_sch = models.CharField(max_length = 30)
	
	def __str__(self):
		#retu = "{} {} {} {}".format(from_sch,stu_num,stu_name,into_sch)
		return self.stu_name
		#return (self.from_sch,self.stu_num,self.stu_name,self.into_sch)
#20170316