'''用于创建一个窗口界面'''
import random
import wx
import _thread



import var
import MyClass

class MyLabel(wx.StaticText):
    '''标签框'''
    def __init__(Parent,label='000'):
        self.SetLabel(label)
        self.SetBackgroundColour('#FFFFFF')
    



class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''
    def __init__(self):
        ''' 构造函数\n'''
        super(Mywin, self).__init__(None, title='SIM', size=(600, 400))
        ################################################################
        self.scroller = wx.ScrolledWindow(self, -1)
        self.scroller.SetBackgroundColour('#666666')
        self.scroller.SetScrollbars( 1, 1, 1600, 1400)
        self.panel = wx.Panel(self.scroller)
        
        self.grid = wx.GridBagSizer(2, 2)  # 参数是子控件之间上下和左右距离
        # 窗口添加内容
        self.添加菜单栏()#self.grid, self.panel)
        self.添加资源栏(self.grid, self.panel)
        self.添加控件(self.grid, self.panel)
        #self.add_ctrl(self.grid, self.panel)
        ###########################################################
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        self.Show()
    def 添加菜单栏(self):
        
        fileMenu = wx.Menu('菜单标题') #顶级菜单
        newitem = wx.MenuItem(fileMenu,wx.ID_NEW, text = "New",helpString='= wx.ITEM_NORMAL') 
        #newitem.SetBitmap(wx.Bitmap("捕捉.png")) 
        fileMenu.Append(newitem) 
        #fileMenu.AppendItem(quit) 

        self.Menu2 = wx.Menu('菜单标题') 
        self.Menu3 = wx.Menu() 
        menubar = wx.MenuBar() 
        menubar.Append(fileMenu, '&File') 
        menubar.Append(self.Menu2, '&File2') 
        menubar.Append(self.Menu3, 'menu3') 

        self.SetMenuBar(menubar) 
        self.Bind(wx.EVT_MENU, self.菜单栏事件) 
    def 菜单栏事件(self,event):
        id = event.GetId()
        if id == wx.ID_NEW: 
            self.Menu2.SetTitle(str(random.random())) #SetLabel(random.random())
        if id == 1099: 
            self.MenuItem1.SetTitle(str(random.random())) 
        #s=event.GetValue()
        print(event.GetEventObject().Title)

    def 添加资源栏(self, grid, panel):
        # 添加表格
        self.cells=[{},{},{}]
        for i in var.need:
            for j in range(3):
                tem= wx.StaticText(panel, label=str(i),size=(40,-1))
                tem.SetBackgroundColour('#FFFFFF')
                self.cells[j].update({i: tem})
                grid.Add( tem, pos=(j, var.need.index(i)),flag=wx.EXPAND)

    def 添加控件(self, grid, panel):
        # 添加表格
        for i in var.need:
            var.units.append(MyClass.factory(panel,i).addfactory(self.grid,var.need.index(i)*2+3))




    def display(self, e=0):
        try:
            _thread.start_new_thread(self.刷新, ("Thread-1", 5, ))
        except:
            print("Error: 无法启动线程")



def 启动窗口():
    print('程序开始 ...')
    app = wx.App()
    win = Mywin()

    app.MainLoop()


启动窗口()






