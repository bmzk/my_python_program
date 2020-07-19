'''
类定义文件
用于定义类
'''
import var

'''

'''


class unit(object):
    '''一个单为的类'''
    def __init__(self,类型,产量,gui):
        '''  '''
        self.worker = 0              #
        self.money = 0
        #
        self.type   = 类型
        self.outPut = 产量 # 单位产出
        self.gui    = gui # 控件部分

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

class factory(object):
    '''一个unit的控件集合类'''
    def __init__(self,panel,grid,row):
        self.worker = 0 #本来应该是unit的属性,但是为了方便按钮事件,设为unit的gui的属性
        self.money = 0
        self.grid = wx.GridBagSizer(5,5)
        grid.Add(self.grid, pos=(row+1, 0),span=(1,5), border=10)
        self.addCtrls(panel,self.grid)

    def addCtrls(self,panel,grid):
        # row 1
        self.head = wx.StaticText(panel, label="F A")
        grid.Add(self.head, pos=(0, 0),span=(1,3), border=10)
        #row 2
        self.w1 = wx.StaticText(panel, label="worker:")
        grid.Add(self.w1, pos=(1, 0), border=10)
        self.w2 = wx.StaticText(panel, label="  0")
        grid.Add(self.w2, pos=(1, 1), border=10)
        self.bt1 = wx.Button(panel, label="增加")
        grid.Add(self.bt1,  pos=(1, 2), flag=wx.EXPAND | wx.ALL)
        self.bt1.Bind(wx.EVT_BUTTON, self.event)
        self.bt2 = wx.Button(panel, label="减少")
        grid.Add(self.bt2,  pos=(1, 3), flag=wx.EXPAND | wx.ALL)
        self.bt2.Bind(wx.EVT_BUTTON, self.event)
        # row 3
        self.r3_1 = wx.StaticText(panel, label="money :")
        grid.Add(self.r3_1, pos=(2, 0), border=10)
        self.r3_2 = wx.StaticText(panel, label=str(self.money))
        grid.Add(self.r3_2, pos=(2, 1), border=10)
        #########################
        # 右侧 绘图窗口
        self.panel = wx.Panel(panel,size=(200,200))
        self.panel.SetBackgroundColour('#aaaaaa')
        grid.Add(self.panel, pos=(0, 4),span=(3,1), border=10)
        
    def event(self,e):
        '''按钮事件,增加 1名worker'''
        if e.GetEventObject().Label == '增加' :
            self.worker += 1
        else:
            self.worker -= 1
        self.w2.SetLabel(str(self.worker))
        c=wx.Colour(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print('color',c)
        self.panel.SetBackgroundColour(c)

        winsound.Beep(1500, 50) #(频率,持续时间)
