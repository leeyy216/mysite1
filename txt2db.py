#coding: utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
import django
django.setup()

import xlrd

def main():
	# from blog.models import Blog
	# f = open('oldblog.txt')
	# for line in f:
	# 	title,content = line.split('****')
	# 	Blog.objects.create(title = title, content = content)
	# f.close()
	rdworkbook = xlrd.open_workbook(r"blogexcel.xlsx")
	all_sheets_list = rdworkbook.sheet_names()
	print("All sheets namme in File:",all_sheets_list)
	first_sheet = rdworkbook.sheet_by_index(0)
	num_rows = first_sheet.nrows
	for curr_row in range(num_rows):
		row = first_sheet.row_values(curr_row)
		print('row%s is %s' %(curr_row,row))
	# for i in range(2,6):
	# 	title = first_sheet.cell(,)


if __name__ =="__main__":
	main()
	print('Done!')	