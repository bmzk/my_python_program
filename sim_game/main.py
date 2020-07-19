'''用于创建一个窗口界面'''
import random
import wx
import _thread
import winsound


import var
import MyClass
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

class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''
    def __init__(self):
        ''' 构造函数\n'''
        super(Mywin, self).__init__(None, title='元胞实验', size=(600, 400))
        ################################################################
        self.scroller = wx.ScrolledWindow(self, -1)
        self.scroller.SetScrollbars( 1, 1, 600, 400)
        self.panel = wx.Panel(self.scroller)
        self.grid = wx.GridBagSizer(2, 2)  # 参数是子控件之间上下和左右距离
        # 窗口添加内容
        #self.添加菜单栏(self.grid, self.panel)
        self.添加控件(self.grid, self.panel)
        #self.add_ctrl(self.grid, self.panel)
        ###########################################################
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        self.Show()

    def 添加菜单栏(self, grid, panel):
        '''  '''
        # 设置 设定
        self.grid0 = wx.BoxSizer(wx.HORIZONTAL)
        # , flag=wx.EXPAND|wx.ALL)
        grid.Add(self.grid0,  pos=(0, 0), span=(1, var.column))

        self.txt1 = wx.StaticText(panel, label="行数:")
        self.grid0.Add(self.txt1, 0, wx.ALL | wx.EXPAND)

        self.txt2 = wx.TextCtrl(panel, value="10")
        self.grid0.Add(self.txt2, 0)  # , wx.EXPAND|wx.ALL)

        self.txt3 = wx.StaticText(panel, label=" 列数:")
        self.grid0.Add(self.txt3, 0, wx.ALL | wx.EXPAND)

        self.txt4 = wx.TextCtrl(panel, value="20")
        self.grid0.Add(self.txt4, 0)  # , wx.EXPAND|wx.ALL)
        # 添加按钮
        self.bt1 = wx.Button(panel, label="给定初始种子")
        self.grid0.Add(self.bt1, 10)  # , flag=wx.EXPAND|wx.ALL)
        self.bt1.Bind(wx.EVT_BUTTON, self.设定初始值)
        # 添加按钮
        self.bt_refresh = wx.Button(panel, label="刷新")
        grid.Add(self.bt_refresh,  pos=(1, var.column-4),
                 span=(1, 4), flag=wx.EXPAND | wx.ALL)
        self.bt_refresh.Bind(wx.EVT_BUTTON, self.display)

    def 添加资源栏(self, grid, panel):
        # 添加表格
        for i in range(len(var.need1)):
            var.units.append(MyClass.unit('A', 10,MyClass.factory(panel,grid,i*3+3)))
            #var.units[i].gui.addCtrls(self.grid,self.panel,i)
        for i in range(len(var.need2)):
            var.units.append(MyClass.unit('A', 10,factory(panel,grid,30+i*3+3)))
            #var.units[i].gui.addCtrls(self.grid,self.panel,30+i*3+len(var.need1))


    def 添加控件(self, grid, panel):
        # 添加表格
        for i in range(len(var.need1)):
            var.units.append(MyClass.unit('A', 10,factory(panel,grid,i*3+3)))
            #var.units[i].gui.addCtrls(self.grid,self.panel,i)
        for i in range(len(var.need2)):
            var.units.append(MyClass.unit('A', 10,factory(panel,grid,30+i*3+3)))
            #var.units[i].gui.addCtrls(self.grid,self.panel,30+i*3+len(var.need1))


    def display(self, e=0):
        try:
            _thread.start_new_thread(self.刷新, ("Thread-1", 5, ))
        except:
            print("Error: 无法启动线程")

    def 设定初始值(self, e=0):
        try:
            var.size = (int(self.txt2.GetValue()), int(self.txt4.GetValue()))
        except:
            self.SetTitle('输入有误')


    def 刷新(self, v1=0, v2=0):
        print('=='*20)
        print('Tick : ', '{:3d}'.format(self.tick),
              ' '*2, '总数:', var.row*var.column)
        self.tick = self.tick+1
        self.Title = '元胞实验  tick:'+str(self.tick)

        #print('      ','{:6d}',format(self.tick))
        for i in MyClass.cellList:
            i.元胞成长()
        for i in MyClass.cellList:
            i.元胞繁殖()
        for i in MyClass.cellList:
            i.refresh()
        for i in range(var.maxAge+1):
            self.count[i] = 0
            for j in MyClass.cellList:
                if j.level == i:
                    self.count[i] = self.count[i] + 1
            print(' '*15, '等级:', i, '{:6d}'.format(self.count[i]))


def 启动窗口():
    print('程序开始 ...')
    app = wx.App()
    win = Mywin()
    win.设定初始值()
    win.CreateStatusBar()
    win.display()
    app.MainLoop()


启动窗口()






