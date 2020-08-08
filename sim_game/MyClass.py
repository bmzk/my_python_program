'''
类定义文件
用于定义类
'''
import wx
import random
import winsound

import var




class factory(object):
    '''一个unit的控件集合类'''
    def __init__(self,panel,类型,产量 = 10):
        self.工人数 = 0 #本来应该是unit的属性,但是为了方便按钮事件,设为unit的gui的属性

        self.__单人产量 = 产量 # 单位产出
        self.grid = wx.GridBagSizer(2,2) 
        self.panel = ''

        名称 = 'F_' +类型
        self.信息={'资金':0,'类型':类型,'名称':名称, '储量':0,'人工':0}

    def sub预算(self):
        i = self.信息['类型']
        var.price[i] = self.get今日价格()
        for i in var.产品列表:
            # 购买
            var.buy[i] += var.pf[i][var.产品列表.index(i)]* self.信息['人工']
        # 生产
        var.out[i] = self.__单人产量 * self.工人数

    def sub结算(self):
        t = self.信息['类型']
        for i in var.产品列表:
            # 购买
            self.信息['资金'] -= var.buy[i] *var.price[i]
        self.信息['储量'] -= var.buy[t]
        # 生产
        self.信息['储量'] += var.out[i]
        self.信息['资金'] += var.out[i] *var.price[i]

    def addCtrls(self,panel):
        # row 1
        grid = self.grid
        self.head = wx.StaticText(panel, label=" "+self.信息['类型'])
        self.head.SetBackgroundColour('#FFFFFF')
        grid.Add(self.head, pos=(0, 0),span=(1,4), flag=wx.EXPAND)
        #row 2
        self.w1 = wx.StaticText(panel, label="worker:")
        self.w1.SetBackgroundColour('#FFFFFF')
        grid.Add(self.w1, pos=(1, 0), flag=wx.EXPAND)
        self.w2 = wx.StaticText(panel, label="  0")
        self.w2.SetBackgroundColour('#FFFFFF')
        grid.Add(self.w2, pos=(1, 1), flag=wx.EXPAND)
        self.bt1 = wx.Button(panel, label="增加")
        grid.Add(self.bt1,  pos=(1, 2), flag=wx.EXPAND)
        self.bt1.Bind(wx.EVT_BUTTON, self.event)
        self.bt2 = wx.Button(panel, label="减少")
        grid.Add(self.bt2,  pos=(1, 3), flag=wx.EXPAND | wx.ALL)
        self.bt2.Bind(wx.EVT_BUTTON, self.event)
        # row 3
        self.r3_1 = wx.StaticText(panel, label="money :")
        self.r3_1.SetBackgroundColour('#FFFFFF')
        grid.Add(self.r3_1, pos=(2, 0), flag=wx.EXPAND)
        self.r3_2 = wx.StaticText(panel, label=str(self.信息['资金']))
        self.r3_2.SetBackgroundColour('#FFFFFF')
        grid.Add(self.r3_2, pos=(2, 1), flag= wx.ALL)
     
        #########################
        # 右侧 绘图窗口
        image = wx.Image("捕获.png")
        temp = image.Scale(100,100).ConvertToBitmap() # 缩放并转换为bitmap
        self.panel = wx.StaticBitmap(parent=panel,bitmap=temp,size=(100,100))
        #self.panel = wx.Panel(panel,size=(200,200))
        self.panel.SetBackgroundColour('#00aaaa')
        grid.Add(self.panel, pos=(0, 4),span=(3,1), border=10)
        self.w2.SetBackgroundColour('#00aaaa')
    
    def event(self,e):
        '''按钮事件,增加 1名worker'''
        if e.GetEventObject().Label == '增加' :
            self.信息['人工'] += 1
        else:
            self.信息['人工'] -= 1
        self.w2.SetLabel(str(self.信息['人工']))
        c='#'
        c += '{:0>2x}'.format(random.randint(0,255))
        c += '{:0>2x}'.format(random.randint(0,255))
        c += '{:0>2x}'.format(random.randint(0,255))
        c=wx.Colour(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print('color',c)
        self.w1.Refresh()
        self.w1.SetBackgroundColour(c)
        self.w2.SetBackgroundColour(c)  
        self.panel.SetBackgroundColour(c)
        winsound.Beep(1500, 50) #(频率,持续时间)
        self.panel.Refresh()
        self.sub预算()


    def get今日价格(self):
        return 1#random.randint(1,50)



    def get净利润(self):
        i = self.信息['类型']
        return var.out[i] *var.price[i] - var.buy[i] *var.price[i]


    def get信息(self):
        #,'今日价格','购买花费'
        rv = []
        i = self.信息['类型']
        self.信息.update({    '产量':var.out[i]       })
        self.信息.update({'今日购买':var.buy[self.信息['类型']]})
        self.信息.update({'今日价格':self.get今日价格()})
        self.信息.update({'购买花费':var.buy[i] * var.price[i] })
        self.信息.update({'今日卖出':var.out[i] * var.price[i] })
        self.信息.update({  '净利润':self.get净利润()  })
        for i in var.信息表[0]:
            #print(i,type(i))
            #print(self.信息[i])
            rv.append(self.信息[i])
        return rv

