#coding: utf-8
#######################################################
#filename:db2exl.py
#author:liyy
#date:2017-3-16
#function：读Django自带数据库,把数据按照指定格式
#######################################################
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
import django
django.setup()

import xlwt

def wtexl():
	from blog.models import Enrollinfo
	rdworkbook = xlrd.open_workbook(r"blogexcel.xlsx")
	all_sheets_list = rdworkbook.sheet_names()
	print("All sheets namme in File:",all_sheets_list)
	#确定所需infosheet
	info_sheet = rdworkbook.sheet_by_index(1)
	print("infosheet is %s" %info_sheet.name)
	#遍历infosheet中所有行
	num_rows = info_sheet.nrows
	for curr_row in range(num_rows):
		row = info_sheet.row_values(curr_row)
		from_sch,stu_num,stu_name,into_sch = row[0],row[1],row[2],row[3]
		#print('%s from %s whose num is %s go into %s' %(stu_name,from_sch,stu_num,into_sch))
		Enrollinfo.objects.get_or_create(from_sch = from_sch,stu_num = stu_num,stu_name = stu_name,into_sch = into_sch)
		#print('row%s is %s' %(curr_row,row))
		print('------------row%s has been saved to db!------------' %curr_row)

	#遍历infosheet中所有列
	num_cols = info_sheet.ncols
	for curr_col in range(num_cols):
		col = info_sheet.col_values(curr_col)
		print('col%s is %s' %(curr_col,col))


def main():
	
	rdexl()
	# for i in range(2,6):
	# 	title = first_sheet.cell(,)


if __name__ =="__main__":
	main()
	print('Done!')	