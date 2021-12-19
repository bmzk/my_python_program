
from bs4 import BeautifulSoup
# Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
import requests
import time
import openpyxl
# import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f',
    'Connection': 'keep-alive'}

########################################
def 获取网页数量(data): return 2
hlist = []
#house=''
hlist.append(['ID', '标题', '信息', '小区名称', '区域', "单价", '总价', '标签'])
class house类(object):
    def __init__(self):
        self.代码段=''
        self.id=''
        self.title=''
        self.info =""
        self.tag = ''
        self.haskey = ""
        self.小区名称=''
        self.区域 = ''
        self.总价 = 0
        self.单价 = 0
    def to_list(self):
        return [self.id,self.title,self.info,self.小区名称,self.区域,self.单价,self.总价,self.tag]

def get_data():
    ''' 输入城市,返回要访问的网页\n
    天津:tj     \n
    新房:loupan     二手房: ershoufang   \n
    返回网页数据'''
    htmlinfo = bytes()  # 查询到的数据
    # 查询第1页
    url = 'https://tj.lianjia.com/ershoufang/binhaixinqu/'
    r = requests.get(url=url+'l3a3a4a5p2p3/', headers=headers)
    htmlinfo = r.content
    # 查询数据
    for i in range(2, 获取网页数量(htmlinfo)+1):  # 获取2-100页的数据
        a = (url + 'pg' + str(i) + 'l3a3a4a5p2p3/')
        r = requests.get(url=a, headers=headers)
        htmlinfo = htmlinfo + r.content
        print('已获取到:',i,'/',获取网页数量(''),' ', a)
    print('已完成 获取网页数据')
    return htmlinfo

def w(mystr, filename='test.txt'):
    f = open(filename, 'w', encoding='utf-8')
    # f.write('mystr')
    f.write(str(mystr))
    f.close()


def listinfo(listhtml):
    '''处理获取的网页数据'''
    areasoup = BeautifulSoup(listhtml, 'html.parser')
    # 转换为格式化数据
    ljhouse = areasoup.find_all(  'div', attrs={'class': 'info clear'})
    for house in ljhouse:
        # 获取一个房屋的信息
        #print('=='*15)
        h=house类()
        try:
            h.代码段=house
            data1 = house.find("a", attrs={"class": ""})
            h.title = data1.get_text()
            h.id=data1["data-housecode"]
            #print('title',h.title,'id',h.id)

            temp = house.find("div", attrs={"class": "positionInfo"})
            temp = temp.find_all("a")
            h.小区名称 = temp[0].get_text()
            h.区域  = temp[1].get_text()
            #print('h.小区名称',h.小区名称,'h.区域' ,h.区域)

            temp = house.find("div", attrs={"class": "houseInfo"})
            h.info = temp.get_text() #.split('|')
            #print('h.info',h.info)

            temp = house.find("div", attrs={"class": "tag"})
            h.tag = temp.get_text()#.split('/')
            #print('h.info',h.tag)

            temp = house.find("div", attrs={"class": "totalPrice"})
            temp = temp.find('span')
            h.总价 =temp.get_text()
            #print('总价',float(h.总价))

            temp = house.find("div", attrs={"class": "unitPrice"})
            #temp = temp.find('span')
            h.单价 =temp['data-price']
            #print('单价',float(h.单价))
        except:
            print('本行出现错误')
        #hlist.append(h.to_list())
        工作簿.写入一行数据(h.to_list())
        print('已完成 ',ljhouse.index(house),'/',len(ljhouse))
        #显示进度(house , ljhouse)
        #print('=='*15)

class 工作簿类(openpyxl.Workbook):
    def 初始化(self):
        self.create_sheet('链家二手房',0)
        self.close()
    def 写入一行数据(self, 行数据: list):
        self.worksheets[0].append(行数据)
    def 获取行数(self):
        return self.worksheets[0].max_row + 1
a=工作簿类()

a.初始化()
print('000',a.worksheets)
super
if __name__ == '__main__':
    print('=='*15)
    print('获取链家房产数据', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('=='*15)
    #input('请输入 要查询的城市：')
    city = 'tj'  # 目前固定为天津
    print('要查询的城市为:', '天津')
    # 获取网页原始数据
    print('-'*40)
    print('开始查询数据')
    html_data = get_data()
    # 处理数据
    工作簿 = 工作簿类()
    工作簿.写入一行数据(hlist[0])
    print('-'*40)
    print('开始处理数据')
    listinfo(html_data)
    # 输出数据
    print('-'*40)
    print('处理数据完成,开始输出数据')
    filename = '链家二手房' + \
        time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())+'.xlsx'
    工作簿.save(filename)
    print('='*4,'end', '='*30)
    #input('按回车结束...')
