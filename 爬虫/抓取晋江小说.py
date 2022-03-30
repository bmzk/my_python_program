
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

def get_url(id):
    a= 'http://www.jjwxc.net/onebook.php?novelid=6198908&chapterid='
    return a+str(id)

def get_data():
    '''返回网页数据'''
    htmlinfo = bytes()  # 查询到的数据
    # 查询数据
    for i in range(1,20):  # 获取2-100页的数据
        r = requests.get(url=get_url(i), headers=headers)
        htmlinfo = htmlinfo + r.content
        print('已获取到:',i)
    print('已完成 获取网页数据')
    return htmlinfo


def listinfo(listhtml):
    '''处理获取的网页数据'''
    areasoup = BeautifulSoup(listhtml, 'html.parser')
    # 转换为格式化数据
    data = areasoup.find_all(  'div', attrs={'class': 'noveltext'})
    rv=[]
    for i in data:
        text=i.get_text()
        rv.append(text)
        print('已处理完成 ',data.index(i),'/',len(data))
    return rv

if __name__ == '__main__':
    print('=='*15)
    # 获取网页原始数据
    print('开始查询数据')
    html_data = get_data()
    # 处理数据
    print('-'*40)
    print('开始处理数据')
    all_data=listinfo(html_data)
    # 输出数据
    print('-'*40)
    print('处理数据完成,开始输出数据')
    filename = 'C:\\Users\\FuPC\\Desktop\\novel' + time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())+'.txt'
    for i in all_data:
        f=open(filename,'a',encoding='utf-8')
        f.write(i)
        f.close()
    print('输出文件：',filename)
    print('='*4,'end', '='*30)
