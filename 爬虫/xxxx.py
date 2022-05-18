# -*- coding:utf-8 -*-
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

aa= [["https://www.jigwxw.com/yuedu/0/24/7084.html", "儿子的邪欲",  "儿子的邪欲"],["https://www.jigwxw.com/yuedu/0/24/7085.html", "银幕保护程式",  "银幕保护程式"],["https://www.jigwxw.com/yuedu/0/24/7086.html", "淫邪的女大学生",  "淫邪的女大学生"],["https://www.jigwxw.com/yuedu/0/24/7087.html", "小筝的耻辱",  "小筝的耻辱"],["https://www.jigwxw.com/yuedu/0/24/7088.html", "迷奸",  "迷奸"],["https://www.jigwxw.com/yuedu/0/24/7089.html", "心理医生救人记",  "心理医生救人记"],["https://www.jigwxw.com/yuedu/0/24/7090.html", "我的老师",  "我的老师"],["https://www.jigwxw.com/yuedu/0/24/7091.html", "客房服务",  "客房服务"],["https://www.jigwxw.com/yuedu/0/24/7092.html", "心理医生",  "心理医生"],["https://www.jigwxw.com/yuedu/0/24/7093.html", "隶娘商店",  "隶娘商店"],["https://www.jigwxw.com/yuedu/0/24/7094.html", "凯特的日记",  "凯特的日记"],["https://www.jigwxw.com/yuedu/0/24/7095.html", "心灵攻掠家",  "心灵攻掠家"],["https://www.jigwxw.com/yuedu/0/24/7096.html", "催淫妖蛊",  "催淫妖蛊"]]
#["https://www.jigwxw.com/yuedu/0/24/7097.html", "色情的授课",  "色情的授课"],  
#["https://www.jigwxw.com/yuedu/0/24/7098.html", "OCR-052",  "OCR-052"],
#["https://www.jigwxw.com/yuedu/0/24/7099.html", "娇妻教室",  "娇妻教室"],
# ["https://www.jigwxw.com/yuedu/0/24/7100.html", "爱情催眠术",  "爱情催眠术"],
#a=[["https://www.jigwxw.com/yuedu/0/24/7101.html", "OL的抉择",  "OL的抉择"],["https://www.jigwxw.com/yuedu/0/24/7102.html", "妈妈美容记",  "妈妈美容记"],["https://www.jigwxw.com/yuedu/0/24/7103.html", "甜蜜的香气",  "甜蜜的香气"],["https://www.jigwxw.com/yuedu/0/24/7104.html", "时光流逝",  "时光流逝"],["https://www.jigwxw.com/yuedu/0/24/7105.html", "表姊的底裤",  "表姊的底裤"],["https://www.jigwxw.com/yuedu/0/24/7106.html", "奸淫女军官",  "奸淫女军官"],["https://www.jigwxw.com/yuedu/0/24/7107.html", "黛芬学园沦亡记",  "黛芬学园沦亡记"],
a=[]
#["https://www.jigwxw.com/yuedu/0/24/7108.html", "新世界（催眠类）1-5完",  "新世界（催眠类）1-5完"],["https://www.jigwxw.com/yuedu/0/24/7109.html", "催眠异想集 之一:催眠师的生活",  "催眠异想集 之一:催眠师的生活"],["https://www.jigwxw.com/yuedu/0/24/7110.html", "颜料",  "颜料"]]
b=[]
#["https://www.jigwxw.com/yuedu/0/24/7111.html", "催眠异想集 之二:天上掉下来的礼物",  "催眠异想集 之二:天上掉下来的礼物"],["https://www.jigwxw.com/yuedu/0/24/7112.html", "新光三越百货中心",  "新光三越百货中心"],["https://www.jigwxw.com/yuedu/0/24/7113.html", "催眠异想集 之三:入戏太深",  "催眠异想集 之三:入戏太深"], ["https://www.jigwxw.com/yuedu/0/24/7114.html", "A Weighty Warning",  "A Weighty Warning"],["https://www.jigwxw.com/yuedu/0/24/7115.html", "催眠异想集 之四:A片拍摄现场",  "催眠异想集 之四:A片拍摄现场"],["https://www.jigwxw.com/yuedu/0/24/7116.html", "魔幻精油",  "魔幻精油"],["https://www.jigwxw.com/yuedu/0/24/7117.html", "舞台催眠秀",  "舞台催眠秀"],["https://www.jigwxw.com/yuedu/0/24/7118.html", "戴亞思想控制指環",  "戴亞思想控制指環"],["https://www.jigwxw.com/yuedu/0/24/7119.html", "天雨传奇",  "天雨传奇"],["https://www.jigwxw.com/yuedu/0/24/7120.html", "The Greatest Gif",  "The Greatest Gif"],["https://www.jigwxw.com/yuedu/0/24/7121.html", "快乐的家庭",  "快乐的家庭"]]
h=[["https://www.jigwxw.com/yuedu/0/24/7122.html", "淫源物语",  "淫源物语"],["https://www.jigwxw.com/yuedu/0/24/7123.html", "完美改造",  "完美改造"],["https://www.jigwxw.com/yuedu/0/24/7124.html", "我的神奇能力",  "我的神奇能力"],["https://www.jigwxw.com/yuedu/0/24/7125.html", "奴隶工厂",  "奴隶工厂"],["https://www.jigwxw.com/yuedu/0/24/7126.html", "黄金屋内多风情",  "黄金屋内多风情"],["https://www.jigwxw.com/yuedu/0/24/7127.html", "阿强的后宫",  "阿强的后宫"],["https://www.jigwxw.com/yuedu/0/24/7128.html", "各怀鬼胎",  "各怀鬼胎"],["https://www.jigwxw.com/yuedu/0/24/7129.html", "老师的奇妙体验",  "老师的奇妙体验"],["https://www.jigwxw.com/yuedu/0/24/7130.html", "水晶迷恋",  "水晶迷恋"],["https://www.jigwxw.com/yuedu/0/24/7131.html", "催眠玩偶系列(一) 放学后的催眠玩偶",  "催眠玩偶系列(一) 放学后的催眠玩偶"],["https://www.jigwxw.com/yuedu/0/24/7132.html", "催眠玩偶系列（二） 假日的催眠玩偶",  "催眠玩偶系列（二） 假日的催眠玩偶"]]
g=[["https://www.jigwxw.com/yuedu/0/24/7133.html", "催眠学园",  "催眠学园"],["https://www.jigwxw.com/yuedu/0/24/7134.html", "催眠事件簿",  "催眠事件簿"],["https://www.jigwxw.com/yuedu/0/24/7135.html", "问题",  "问题"],["https://www.jigwxw.com/yuedu/0/24/7136.html", "催眠事件簿(番外篇)-芷涵的日记",  "催眠事件簿(番外篇)-芷涵的日记"],["https://www.jigwxw.com/yuedu/0/24/7137.html", "名流女仆",  "名流女仆"],["https://www.jigwxw.com/yuedu/0/24/7138.html", "催眠性爱派对",  "催眠性爱派对"],["https://www.jigwxw.com/yuedu/0/24/7139.html", "幸运的我",  "幸运的我"],["https://www.jigwxw.com/yuedu/0/24/7140.html", "催眠游戏",  "催眠游戏"],["https://www.jigwxw.com/yuedu/0/24/7141.html", "秘书",  "秘书"],["https://www.jigwxw.com/yuedu/0/24/7142.html", "两星期",  "两星期"],["https://www.jigwxw.com/yuedu/0/24/7143.html", "邪恶的女医生",  "邪恶的女医生"],["https://www.jigwxw.com/yuedu/0/24/7144.html", "老师奴隶",  "老师奴隶"],["https://www.jigwxw.com/yuedu/0/24/7145.html", "收获",  "收获"],["https://www.jigwxw.com/yuedu/0/24/7146.html", "儿子的命令",  "儿子的命令"],["https://www.jigwxw.com/yuedu/0/24/7147.html", "现代妖术师",  "现代妖术师"],["https://www.jigwxw.com/yuedu/0/24/7148.html", "催眠师的后台",  "催眠师的后台"],["https://www.jigwxw.com/yuedu/0/24/7149.html", "PSY SEED",  "PSY SEED"],["https://www.jigwxw.com/yuedu/0/24/7150.html", "诱捕琳达",  "诱捕琳达"],["https://www.jigwxw.com/yuedu/0/24/7151.html", "九月鹰飞补遗",  "九月鹰飞补遗"],["https://www.jigwxw.com/yuedu/0/24/7152.html", "催眠奴役",  "催眠奴役"],["https://www.jigwxw.com/yuedu/0/24/7153.html", "绿色的幸福",  "绿色的幸福"],["https://www.jigwxw.com/yuedu/0/24/7154.html", "奴隶诊所",  "奴隶诊所"],["https://www.jigwxw.com/yuedu/0/24/7155.html", "穿越机器猫",  "穿越机器猫"],["https://www.jigwxw.com/yuedu/0/24/7156.html", "马汀大师的阴谋",  "马汀大师的阴谋"]]
f=[["https://www.jigwxw.com/yuedu/0/24/7157.html", "美丽的赌注",  "美丽的赌注"],["https://www.jigwxw.com/yuedu/0/24/7158.html", "Above That Ye Are Able",  "Above That Ye Are Able"],["https://www.jigwxw.com/yuedu/0/24/7159.html", "坏小孩、魔法石跟校长",  "坏小孩、魔法石跟校长"],["https://www.jigwxw.com/yuedu/0/24/7160.html", "名媛侦探",  "名媛侦探"],["https://www.jigwxw.com/yuedu/0/24/7161.html", "幸福的家庭",  "幸福的家庭"],["https://www.jigwxw.com/yuedu/0/24/7162.html", "公主恋人之催眠隶奴",  "公主恋人之催眠隶奴"],["https://www.jigwxw.com/yuedu/0/24/7163.html", "绝对控制",  "绝对控制"],["https://www.jigwxw.com/yuedu/0/24/7164.html", "无能之力",  "无能之力"],["https://www.jigwxw.com/yuedu/0/24/7165.html", "只属于你",  "只属于你"],["https://www.jigwxw.com/yuedu/0/24/7166.html", "花柔水",  "花柔水"],["https://www.jigwxw.com/yuedu/0/24/7167.html", "奴役丸",  "奴役丸"],["https://www.jigwxw.com/yuedu/0/24/7168.html", "催眠愉快",  "催眠愉快"],["https://www.jigwxw.com/yuedu/0/24/7169.html", "欲望健身房",  "欲望健身房"],["https://www.jigwxw.com/yuedu/0/24/7170.html", "奇怪的枕头",  "奇怪的枕头"],["https://www.jigwxw.com/yuedu/0/24/7171.html", "催眠奴隶",  "催眠奴隶"],["https://www.jigwxw.com/yuedu/0/24/7172.html", "恶魔般的姊姊",  "恶魔般的姊姊"],["https://www.jigwxw.com/yuedu/0/24/7173.html", "佳蓉学姊",  "佳蓉学姊"],["https://www.jigwxw.com/yuedu/0/24/7174.html", "图书馆员的奴隶",  "图书馆员的奴隶"],["https://www.jigwxw.com/yuedu/0/24/7175.html", "指令",  "指令"],["https://www.jigwxw.com/yuedu/0/24/7176.html", "一家之主",  "一家之主"],["https://www.jigwxw.com/yuedu/0/24/7177.html", "催淫之馆",  "催淫之馆"],["https://www.jigwxw.com/yuedu/0/24/7178.html", "玛莉安的初体验",  "玛莉安的初体验"],["https://www.jigwxw.com/yuedu/0/24/7179.html", "《性爱催眠术》",  "《性爱催眠术》"],["https://www.jigwxw.com/yuedu/0/24/7180.html", "慾?靈",  "慾?靈"],["https://www.jigwxw.com/yuedu/0/24/7181.html", "《昭圣者小米》",  "《昭圣者小米》"],["https://www.jigwxw.com/yuedu/0/24/7182.html", "性奴新娘",  "性奴新娘"],["https://www.jigwxw.com/yuedu/0/24/7183.html", "报酬",  "报酬"],["https://www.jigwxw.com/yuedu/0/24/7184.html", "百科全书",  "百科全书"],["https://www.jigwxw.com/yuedu/0/24/7185.html", "《玩具工厂》",  "《玩具工厂》"],["https://www.jigwxw.com/yuedu/0/24/7186.html", "改写射雕新篇",  "改写射雕新篇"],["https://www.jigwxw.com/yuedu/0/24/7187.html", "古墓丽影:科特兹的征服",  "古墓丽影:科特兹的征服"],["https://www.jigwxw.com/yuedu/0/24/7188.html", "前女友",  "前女友"],["https://www.jigwxw.com/yuedu/0/24/7189.html", "邻家新妻",  "邻家新妻"],["https://www.jigwxw.com/yuedu/0/24/7190.html", "红石",  "红石"],["https://www.jigwxw.com/yuedu/0/24/7191.html", "救援行动",  "救援行动"],["https://www.jigwxw.com/yuedu/0/24/7192.html", "性幻想",  "性幻想"],["https://www.jigwxw.com/yuedu/0/24/7193.html", "玩具工厂",  "玩具工厂"],["https://www.jigwxw.com/yuedu/0/24/7194.html", "出差",  "出差"],["https://www.jigwxw.com/yuedu/0/24/7195.html", "好女孩",  "好女孩"],["https://www.jigwxw.com/yuedu/0/24/7196.html", "美丽的奴隶",  "美丽的奴隶"],["https://www.jigwxw.com/yuedu/0/24/7197.html", "幸福人生传",  "幸福人生传"],["https://www.jigwxw.com/yuedu/0/24/7198.html", "好朋友",  "好朋友"],["https://www.jigwxw.com/yuedu/0/24/7199.html", "美丽人生",  "美丽人生"],["https://www.jigwxw.com/yuedu/0/24/7200.html", "被催眠的少女小柔",  "被催眠的少女小柔"],["https://www.jigwxw.com/yuedu/0/24/7201.html", "华丽的烟丝",  "华丽的烟丝"],["https://www.jigwxw.com/yuedu/0/24/7202.html", "绝对服从",  "绝对服从"],["https://www.jigwxw.com/yuedu/0/24/7203.html", "《世界调制模式》（1-射雕篇1-3+新年篇1-4+番外1-8）",  "《世界调制模式》（1-射雕篇1-3+新年篇1-4+番外1-8）"],["https://www.jigwxw.com/yuedu/0/24/7204.html", "催眠性爱派对",  "催眠性爱派对"],["https://www.jigwxw.com/yuedu/0/24/7205.html", "流星",  "流星"],["https://www.jigwxw.com/yuedu/0/24/7206.html", "旅馆",  "旅馆"],["https://www.jigwxw.com/yuedu/0/24/7207.html", "催眠学园",  "催眠学园"],["https://www.jigwxw.com/yuedu/0/24/7208.html", "Domestic Love Others",  "Domestic Love Others"],["https://www.jigwxw.com/yuedu/0/24/7209.html", "丝丝入淫",  "丝丝入淫"],["https://www.jigwxw.com/yuedu/0/24/7210.html", "昭圣者小米",  "昭圣者小米"]]
d= [["https://www.jigwxw.com/yuedu/0/24/7211.html", "极品公子改编版",  "极品公子改编版"]]

url_list =a+b+h+g+f
def listinfo(_url):
    '''返回网页数据'''
    htmlinfo = bytes()  # 查询到的数据
    # 查询数据
    htmlinfo = requests.get(url=_url[0], headers=headers).content
    print('已完成 获取网页数据', _url)
    '''处理获取的网页数据'''
    areasoup = BeautifulSoup(htmlinfo, 'html.parser')
    # 转换为格式化数据
    data = areasoup.find_all('div', attrs={'class': "novel_content"})

    rv = []#_url[1]]
    for i in data:
        text = i.get_text()
        rv.append(text)
        print('已处理完成 ', data.index(i), '/', len(data))
    return rv


filename = 'C:\\Users\\FuPC\\Desktop\\novel' + \
    time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())+'.txt'

###########################################
if __name__ == '__main__':
    print('=='*15)
    for u in url_list:
        time.sleep(0.5)
        all_data = listinfo(u)
        # 输出数据
        print('-'*40)
        print('处理数据完成,开始输出数据')
        for i in all_data:
            f = open(filename, 'a', encoding='utf-8')
            f.write(i+'\n')
            f.close()
        print('='*4,  url_list.index(u),' / ',len(url_list),'='*30)
    print('输出文件:', filename)
