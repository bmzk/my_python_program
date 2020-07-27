input(1)
try:
	from bs4 import BeautifulSoup
	print('bs4')
except:
	input(2)

input(1)
try:
	import bs4
except:
	input(2)
import openpyxl
w = openpyxl.Workbook()
w.close()
w[w.sheetnames[1]].append([1,2,3])
w.save('filename.xlsx')