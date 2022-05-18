
'''
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
'''

fl='qweasd.txt'
f=open(fl,'r',encoding='utf-8')
d=f.readlines()
f.close()

n=0
w=open('q4.txt','w',encoding='utf-8')
for i in d:
	n=n+1
	s=i
	s=s.replace('    ','\n')
	s=s.replace('。','。\n')
	w.write(s)
	print(d.index(i),' / ', len(d))
w.close()
