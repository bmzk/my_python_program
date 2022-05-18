
from bs4 import BeautifulSoup
# Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
import requests
import time
import openpyxl

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f',
    'Connection': 'keep-alive'}
########################################
url_data=[]


for i in range()
def 获取地址():
    f=open('t1.html','r',encoding='utf-8')
    rv=f.readlines()
    f.close()
    return rv

def get_data(n:int ):
    '''返回网页数据'''
    htmlinfo = bytes()  # 查询到的数据
    # 查询数据
    _url='https://www.52bqg.net/book_96028/'+url_data[n][:13]
    htmlinfo = requests.get(url=_url, headers=headers)
    print('已完成 获取网页数据',_url)
    return htmlinfo


def listinfo(n):
    '''返回网页数据'''
    htmlinfo = bytes()  # 查询到的数据
    # 查询数据
    _url='https://www.52bqg.net/book_96028/'+url_data[n][:13]
    htmlinfo = requests.get(url=_url, headers=headers)
    print('已完成 获取网页数据',_url)
    '''处理获取的网页数据'''
    areasoup = BeautifulSoup(htmlinfo, 'html.parser')
    # 转换为格式化数据
    data = areasoup.find_all(  'h1')
    rv=[]
    for i in data:
        text=i.get_text()
        rv.append(text)
        print('已处理完成 ',data.index(i),'/',len(data))
    data = areasoup.find_all(  'div', attrs={'id': 'content'})
    for i in data:
        text=i.get_text()
        rv.append(text)
        print('已处理完成 ',data.index(i),'/',len(data))
    return rv

filename = 'C:\\Users\\FuPC\\Desktop\\novel' + time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())+'.txt'

def main(n):
    all_data=listinfo(n)
    # 输出数据
    print('-'*40)
    print('处理数据完成,开始输出数据')
    for i in all_data:
        f=open(filename,'a',encoding='utf-8')
        f.write(i+'\n')
        f.close()
    print('输出文件：',filename)
    print('='*4,'end', '='*30)



###########################################
if __name__ == '__main__':
    print('=='*15)
    url_data=获取地址()
    for i in range(len(url_data)):
        main(i)
