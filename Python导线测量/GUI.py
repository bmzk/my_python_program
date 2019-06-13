'''用于创建一个窗口界面'''
# import #####################################################
import wx
import myvar
# 函数 #######################################################

# 辅助类 定义 #################################################
观测记录 = {'测站': 'O',
        '目标_后视': 'H',
        '目标_前视': 'Q',
        '盘左_后视': 'LH',
        '盘右_后视': 'RH',
        '盘左_前视': '0',
        '盘右_前视': '0',
        '2C_盘左': '0',
        '2C_盘右': '0',
        '半测回_盘左': '0',
        '半测回_盘右': '0',
        '一测回角度': '0'}
textctrl = lambda p, mystr='': wx.TextCtrl(
    p, value=mystr, style=wx.TE_READONLY | wx.TE_CENTER)


class jd_table(object):
    '''角度观测记录表'''

    def __init__(self, grid, panel, 记录=观测记录):
        # 测站 目标 盘左 盘右 2c 半测回 1测回
        self.测站 = textctrl(panel, '测站')
        #    panel, '测站',  style=wx.TE_READONLY | wx.TE_CENTER)
        self.目标 = textctrl(panel, '目标')
        self.读数 = wx.TextCtrl(
            panel, -1, '观测读数',  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.盘左 = wx.TextCtrl(
            panel, -1, '盘左',  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.盘右 = wx.TextCtrl(
            panel, -1, '盘右',  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.C2 = wx.TextCtrl(
            panel, -1, '2C', style=wx.TE_READONLY | wx.TE_CENTRE)
        self.半测回 = wx.TextCtrl(panel, -1, '半测回角度',
                               style=wx.TE_READONLY | wx.TE_CENTRE)
        self.一测回 = wx.TextCtrl(panel, -1, '一测回角度',
                               style=wx.TE_READONLY | wx.TE_CENTRE)
        bw = -3
        grid.Add(self.测站, pos=(1, 0), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.目标, pos=(1, 1), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.读数, pos=(1, 2), span=(1, 2),
                 flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.盘左, pos=(2, 2), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.盘右, pos=(2, 3), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.C2, pos=(1, 4), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.半测回, pos=(1, 5), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.一测回, pos=(1, 6), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)

        self.jdds = []  # 角度读数
        for i in range(myvar.导线边数):
            self.jdds.append(jd(grid, panel, 3+i*2, 记录))


class jd(object):
    '''一测站观测记录'''

    def __init__(self, grid, panel, x, 记录: dict = 观测记录):
        self.测站 = wx.TextCtrl(
            panel, -1, 记录["测站"],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.目标_后视 = wx.TextCtrl(
            panel, -1, 记录['目标_后视'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.目标_前视 = wx.TextCtrl(
            panel, -1, 记录['目标_前视'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.盘左_后视 = wx.TextCtrl(
            panel, -1, 记录['盘左_后视'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.盘右_后视 = wx.TextCtrl(
            panel, -1, 记录['盘右_后视'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.盘左_前视 = wx.TextCtrl(
            panel, -1, 记录['盘左_前视'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.盘右_前视 = wx.TextCtrl(
            panel, -1, 记录['盘右_前视'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.C2_盘左 = wx.TextCtrl(
            panel, -1, 记录['2C_盘左'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.C2_盘右 = wx.TextCtrl(
            panel, -1, 记录['2C_盘右'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.半测回_盘左 = wx.TextCtrl(
            panel, -1, 记录['半测回_盘左'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.半测回_盘右 = wx.TextCtrl(
            panel, -1, 记录['半测回_盘右'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        self.一测回角度 = wx.TextCtrl(
            panel, -1, 记录['一测回角度'],  style=wx.TE_READONLY | wx.TE_CENTRE)
        bw = -3
        grid.Add(self.测站, pos=(x, 0), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)

        grid.Add(self.目标_后视, pos=(x, 1), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.目标_前视, pos=(x+1, 1), flag=wx.ALL | wx.EXPAND, border=bw)

        grid.Add(self.盘左_后视, pos=(x, 2), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.盘右_后视, pos=(x, 3), flag=wx.ALL | wx.EXPAND, border=bw)

        grid.Add(self.盘左_前视, pos=(x+1, 2), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.盘右_前视, pos=(x+1, 3), flag=wx.ALL | wx.EXPAND, border=bw)

        grid.Add(self.C2_盘左, pos=(x, 4), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.C2_盘右, pos=(x+1, 4), flag=wx.ALL | wx.EXPAND, border=bw)

        grid.Add(self.半测回_盘左, pos=(x, 5), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.半测回_盘右, pos=(x+1, 5), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.一测回角度, pos=(x, 6), span=(2, 1),
                 flag=wx.ALL | wx.EXPAND, border=bw)


边长读数 = ['边名', '边长1', '边长2', '边长3', '边长4', '平均边长']


class bian(object):
    def __init__(self, grid, panel, y, 边长读数=边长读数):
        self.边名 = textctrl(panel, 边长读数[0])
        self.边长 = [textctrl(panel, 边长读数[1]),
                   textctrl(panel, 边长读数[2]),
                   textctrl(panel, 边长读数[3]),
                   textctrl(panel, 边长读数[4])]
        self.平均边长 = textctrl(panel, 边长读数[5])
        bw = -3
        grid.Add(self.边名, pos=(0, y), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.边长[0], pos=(1, y), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.边长[1], pos=(2, y), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.边长[2], pos=(3, y), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.边长[3], pos=(4, y), flag=wx.ALL | wx.EXPAND, border=bw)
        grid.Add(self.平均边长, pos=(5, y), flag=wx.ALL | wx.EXPAND, border=bw)


class bian_table(object):
    def __init__(self, grid, panel):
        self.bcds = []  # 边长读数
        for i in range(myvar.导线边数):
            self.bcds.append(bian(grid, panel, i, 边长读数))
# 主界面定义 ###################################################


class MyWindows(wx.Frame):

    def __init__(self):
        ''' 构造函数\n
        GridBagSizer : 子构件可被添加到网格中的特定单元.\n
        一个子物件可以在水平和/或垂直地占据一个以上的单元.\n
        主要使用方法 : Wx.GridbagSizer().Add(control, pos, span, flags, border) \n
        control : 控件 \n
        pos : 控件位置,第几行第几列,从0开始\n
        span : 控件跨越的行数和列数\n'''
        self.w=1000
        self.h=700
        self.w_draw=400
        self.h_height=500
        super(MyWindows, self).__init__(None, size=(1000, 700))
        self.SetTitle('导线测量模拟题')
        # self.MenuBar=wx.MenuBar()
        self.菜单栏()
        self.split_window()
        self.Center()
        self.Show()

    def split_window(self):
        '''面板分割'''
        # 分离器对象添加到顶层帧。
        # 一个布局管理器，拥有两个子窗口,子窗口大小可以通过拖动它们之间的界限来动态变化。

        self.__splitter1 = wx.SplitterWindow(
            self, -1, style=wx.SP_BORDER)  # 把面板分为123和4
        self.panel4_set()
        self.panel123 = wx.Panel(self.__splitter1, -1, size=(1000, self.h_height))
        self.__splitter1.SplitHorizontally(self.panel123, self.panel4)


        splitter2 = wx.SplitterWindow(
            self.panel123, -1, style=wx.SP_BORDER, size=(self.w, self.h_height))  # 把面板分为12和3
        self.panel3 = wx.Panel(splitter2, -1, size=(self.w_draw, self.h_height))
        self.panel12 = wx.Panel(splitter2, -1, size=(self.w-self.w_draw, self.h_height))
        splitter2.SplitVertically(self.panel12, self.panel3)


        self.__splitter3 = wx.SplitterWindow(
            self.panel12, -1, size=(self.w-self.w_draw, self.h_height))  # 把面板分为1和2
        self.panel1_set()
        self.panel2_set()
        self.__splitter3.SplitHorizontally(self.panel1, self.panel2)
        #右侧窗口###################################################

        # self.test(self.panel1,'p1')
        self.test(self.panel3, 'p3')

        # 右侧窗口添加内容
        
        
        ###########################################################
        # splitter1.SplitVertically(self.panel_left, self.panel_right)
        # self.panel_left.SetSizerAndFit(self.grid_left)
        # self.panel4.SetSizerAndFit(grid4)

    def panel1_set(self):
        '''0'''
        self.panel1 = wx.ScrolledWindow(
            self.__splitter3, -1, style=wx.SB_VERTICAL)  # , size=(500, 150))
        self.panel1.SetScrollbars(1, 1, 400, 400)
        # 添加控件#
        self.rb1 = wx.RadioButton(self.panel1, label='样式1')
        self.rb2 = wx.RadioButton(self.panel1, label='样式2')
        self.grid1 = wx.GridBagSizer(5, 5)
        self.grid1.Add(self.rb1, pos=(0, 0))
        self.grid1.Add(self.rb2, pos=(0, 1))
        self.panel1_ctrls = jd_table(self.grid1, self.panel1)

        # 结束
        self.panel1.SetSizerAndFit(self.grid1)

    def panel2_set(self):
        '''设置panel2的控件'''
        self.panel2 = wx.ScrolledWindow(
            self.__splitter3, -1, style=wx.SB_VERTICAL)  # , size=(500, 150))
        self.panel2.SetScrollbars(1, 1, 800, 800)
        # 添加控件#
        self.grid2 = wx.GridBagSizer(6, 5)
        self.panel2_ctrls = bian_table(self.grid2, self.panel2)

        # 结束
        self.panel2.SetSizerAndFit(self.grid2)

    def panel4_set(self):
        '''8y7test'''
        # panel=wx.Panel()
        self.panel4 = wx.Panel(self.__splitter1, -1, size=(1000, self.h-self.h_height))
        self.grid4 = wx.BoxSizer(wx.VERTICAL)
        collpane = wx.CollapsiblePane(self.panel4, label="Details:")
        self.grid4.Add(collpane, 2, wx.GROW | wx.ALL, 5)
        st = wx.StaticText(collpane.GetPane(), wx.ID_ANY, "test!")
        grid = wx.BoxSizer(wx.VERTICAL)
        grid.Add(st, 1, wx.GROW | wx.ALL, 2)
        self.panel4.SetSizer(self.grid4)
        self.grid4.SetSizeHints(self.panel4)

    def add_ctrls2(self, grid, panel, mystr='123456789'):
        '''0'''
        # 左侧窗口添加内容
        # 添加按钮 读取数据
        读取数据 = wx.Button(panel, label=mystr, style=wx.EXPAND)
        grid.Add(读取数据, pos=(2, 1), flag=wx.ALIGN_CENTER)

    def test(self, panel, mystr='test123456789'):
        grid = wx.BoxSizer(wx.VERTICAL)
        读取数据 = wx.Button(panel, label=mystr, style=wx.EXPAND)
        grid.Add(读取数据, 1, wx.ALL | wx.EXPAND, 5)
        读取数据2 = wx.Button(panel, label=mystr+'-2', style=wx.EXPAND)
        grid.Add(读取数据2, 1, flag=wx.ALIGN_CENTER)

        panel.SetSizerAndFit(grid)

    def 菜单栏(self):
        menubar = wx.MenuBar()
        # 文件菜单#####################################################
        fileMenu = wx.Menu()
        newitem = wx.MenuItem(fileMenu, wx.ID_NEW,
                              text="New", kind=wx.ITEM_NORMAL)
        # newitem.SetBitmap(wx.Bitmap("new.bmp"))
        fileMenu.AppendItem(newitem)

        fileMenu.AppendSeparator()

        editMenu = wx.Menu()
        copyItem = wx.MenuItem(editMenu, 100, text="copy", kind=wx.ITEM_NORMAL)
        # copyItem.SetBitmap(wx.Bitmap("copy.bmp"))

        editMenu.AppendItem(copyItem)
        cutItem = wx.MenuItem(editMenu, 101, text="cut", kind=wx.ITEM_NORMAL)
        # cutItem.SetBitmap(wx.Bitmap("cut.bmp"))

        editMenu.AppendItem(cutItem)
        pasteItem = wx.MenuItem(
            editMenu, 102, text="paste", kind=wx.ITEM_NORMAL)
        # pasteItem.SetBitmap(wx.Bitmap("paste.bmp"))

        editMenu.AppendItem(pasteItem)
        fileMenu.AppendMenu(wx.ID_ANY, "Edit", editMenu)
        fileMenu.AppendSeparator()

        radio1 = wx.MenuItem(fileMenu, 200, text="Radio1", kind=wx.ITEM_RADIO)
        radio2 = wx.MenuItem(fileMenu, 300, text="radio2", kind=wx.ITEM_RADIO)

        fileMenu.AppendItem(radio1)
        fileMenu.AppendItem(radio2)
        fileMenu.AppendSeparator()

        fileMenu.AppendCheckItem(103, "Checkable")
        quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')

        fileMenu.AppendItem(quit)
        menubar.Append(fileMenu, 'File000')
        # 配置菜单 #####################################################
        Menu_setting = wx.Menu()
        self.Bind(wx.EVT_MENU, self.menuhandler)

        menubar.Append(Menu_setting, '配置')
        # 导出菜单 #####################################################
        Menu_out = wx.Menu()
        self.Bind(wx.EVT_MENU, self.menuhandler)

        menubar.Append(Menu_out, '导出')
        # 导入菜单 #####################################################
        Menu_in = wx.Menu()
        self.Bind(wx.EVT_MENU, self.menuhandler)

        menubar.Append(Menu_in, '导入')
        # 工具菜单 #####################################################
        Menu_tool = wx.Menu()
        self.Bind(wx.EVT_MENU, self.menuhandler)

        menubar.Append(Menu_tool, '工具')
        # 关于菜单 #####################################################

        Menu_abort = wx.Menu()
        self.Bind(wx.EVT_MENU, self.menuhandler)

        menubar.Append(Menu_abort, '关于')
        ######################################################
        self.SetMenuBar(menubar)

    def menuhandler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW:
            self.text.AppendText("new"+"\n")


# 运行程序 #####################################################
app = wx.App()
window = MyWindows()
window.Show(True)
app.MainLoop()
