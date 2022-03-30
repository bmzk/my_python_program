
from cgitb import text
from bs4 import BeautifulSoup
# Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
import requests
import time
import openpyxl
# import pandas as pd

myfile='novel.txt'
f=open(myfile,'r',encoding='utf-8')
txt=f.readlines()
f.close()
retxt=['插入书签',' [收藏此章节]','[举报]','举报色情有害','举报涉未成年有害','举报刷数据','举报伪更','其他',
'文章收藏','为收藏文章分类','新增','取消','+新增收藏类别','+收藏类别','定制收藏类别','查看收藏列表','+新增收藏类别','定制收藏类别','查看收藏列表','[收藏此章节]']

filename = 'retxt' +  time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())+'.txt'
w=open(filename,'a',encoding='utf-8')
n=0
for j in txt:
    n=n+1
    i=j
    if i=='/n':
        continue
    i=i.replace('  ','\n')
    for j in retxt:
        i=i.replace(j,'')
        #print(i)
    w.write(i)
    print('已完成',n,'/',len(txt))

w.close()

