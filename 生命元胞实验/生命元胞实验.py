'''用于创建一个窗口界面'''
import random
import wx
import _thread

import var
import MyClass


class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''

    def __init__(self):
        ''' 构造函数\n
            GridBagSizer : 子构件可被添加到网格中的特定单元.\n
            一个子物件可以在水平和/或垂直地占据一个以上的单元.\n
            主要使用方法 : Wx.GridbagSizer().Add(control, pos, span, flags, border) \n
            control : 控件 \n
            pos : 控件位置,第几行第几列,从0开始\n
            span : 控件跨越的行数和列数\n'''
        super(Mywin, self).__init__(None, title='元胞实验', size=(600, 400))
        self.tick = 0
        self.count = []
        for i in range(var.maxAge+1):
            self.count.append(0)
        ################################################################
        self.scroller = wx.ScrolledWindow(self, -1)
        self.scroller.SetScrollbars(
            1, 1, (var.column+5) * var.size[1], (var.row+6) * var.size[0])
        self.panel = wx.Panel(self.scroller)
        self.grid = wx.GridBagSizer(2, 2)  # 参数是子控件之间上下和左右距离
        # 窗口添加内容
        self.添加设定栏(self.grid, self.panel)
        self.add_ctrl(self.grid, self.panel)
        #self.add_ctrl(self.grid, self.panel)
        ###########################################################
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        self.Show()

    def 添加设定栏(self, grid, panel):
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

    def add_ctrl(self, grid, panel):
        # 添加表格
        for i in range(var.row * var.column):
            MyClass.cellList.append(MyClass.cell(panel, i))
            行号 = i // var.column
            列号 = i % var.column
            MyClass.cellList[i].box = wx.StaticText(
                panel, label=str(i+1), size=var.size)
            grid.Add(MyClass.cellList[i].box, pos=(行号+3, 列号), border=10)

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
        #self.add_ctrl(self.grid, self.panel)
        MyClass.cellList[random.randint(0, var.row*var.column-2)].level = 1

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
