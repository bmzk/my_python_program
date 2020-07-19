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
        self.worker = 0 #本来应该是unit的属性,但是为了方便按钮事件,设为unit的gui的属性
        self.money = 0
        self.type   = 类型
        self.outPut = 产量 # 单位产出
        self.grid = wx.GridBagSizer(2,2) 
        self.addCtrls(panel,self.grid)

    def addfactory(self,grid,row):
        grid.Add(self.grid, pos=(row+1, 0),span=(1,5),flag=wx.EXPAND | wx.ALL)
    def addCtrls(self,panel,grid):
        # row 1
        self.head = wx.StaticText(panel, label=" "+self.type)
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
        self.r3_2 = wx.StaticText(panel, label=str(self.money))
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
            self.worker += 1
        else:
            self.worker -= 1
        self.w2.SetLabel(str(self.worker))
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


    def 购买(self):
        '''    '''
        a={'sad':55,'f':9,'ty':5}
        list(a.keys())
        for i in list(var.pf[self.type].keys()):
            var.stor_t[i] -= var.pf[self.type][i] * self.worker
            self.money -= var.price[self.type] * var.pf[self.type][i] * self.worker

    def __生产(self):
        return self.outPut * self.worker

    def 卖出(self,x,y):
        var.stor_t[self.type] += self.__生产()
        self.money += var.price[self.type] * self.__生产()