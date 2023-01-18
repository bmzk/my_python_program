
from bs4 import BeautifulSoup
# Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
import requests
import time
# import openpyxl

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f',
    'Connection': 'keep-alive'}
filename = 'C:\\Users\\FuPC\\Desktop\\novel' + time.strftime("-%H_%M_%S", time.localtime())+'.txt'
########################################

def get_url(id):
    a= 'https://jpxs123.cc/tongren/8038/'
    return a+str(id)+'.html'

def get_data():
    '''返回网页数据'''
    htmlinfo = bytes()  # 查询到的数据
    # 查询数据
    for i in range(100,150):  # 获取2-100页的数据
        r = requests.get(url=get_url(i), headers=headers)
        htmlinfo = htmlinfo + r.content
        print('已获取到:',i)
    print('已完成 获取网页数据')
    return htmlinfo


def listinfo(listhtml):
    '''处理获取的网页数据'''
    areasoup = BeautifulSoup(listhtml, 'html.parser')
    # 转换为格式化数据
    data = areasoup.find_all(  'div', attrs={'class': 'read_chapterDetail'})
    rv=[]
    for i in data:
        text=i.get_text()
        rv.append(text)
        print('已处理完成 ',data.index(i),'/',len(data))
    return rv

def w(s:str):
    '''将文本写入文件'''
    f=open(filename,'a',encoding='utf-8')
    f.write(s+'\n')
    f.close()
if __name__ == '__main__':
    # 获取网页原始数据
    print('开始查询数据')
    for i in range(150,350):  # 获取xx-xx页的数据
        r = requests.get(url=get_url(i), headers=headers)
        print('已获取到:',i,end='')
        # 处理获取的网页数据'''
        areasoup = BeautifulSoup(r.content, 'html.parser')
        # 转换为格式化数据
        data = areasoup.find_all(  'div', attrs={'class': 'read_chapterDetail'})
        #w('第'+str(i)+'章')
        for i2 in data:
            w(i2.get_text())
        print('  已处理完成')


