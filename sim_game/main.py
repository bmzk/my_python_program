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
        super(Mywin, self).__init__(None, title='SIM', size=(800, 800))
        ################################################################
        self.scroller = wx.ScrolledWindow(self, -1)
        self.scroller.SetBackgroundColour('#666666')
        self.scroller.SetScrollbars( 1, 1, 1000, 1000)
        self.panel = wx.Panel(self.scroller)
        self.grid0 = wx.BoxSizer(wx.VERTICAL) # 最基本的布局
        self.表=[]
        ##############################################################
        self. 创建单位列表()
        ##################################################################
        # 窗口添加内容
        self.添加菜单栏()
        ###############################################################
        self.grid_信息表 = wx.GridBagSizer(2, 2)  # 参数是子控件之间上下和左右距离
        self.grid0.Add(self.grid_信息表, 10, flag = wx.ALL|wx.EXPAND,border = 5)
        self.添加表头()
        self.添加信息表(self.grid_信息表,self.panel )
        self.grid0.AddStretchSpacer(1) 


        self.bt1 = wx.Button(self.panel, label="刷新")
        self.grid0.Add(self.bt1, 2, flag=wx.EXPAND)
        self.bt1.Bind(wx.EVT_BUTTON, self.刷新)
        self.grid0.AddStretchSpacer(1) 
        self.bt2 = wx.Button(self.panel, label="刷新2")
        self.grid0.Add(self.bt2, 2, flag=wx.EXPAND)
        self.bt1.Bind(wx.EVT_BUTTON, self.刷新2)
        ############################################
        self.添加资源栏(self.grid0)
        ###########################################################
        self.panel.SetSizerAndFit(self.grid0)
        self.Center()
        self.Show()

    def 创建单位列表(self):
        for i in var.产品列表:
            var.单位列表.append(MyClass.factory(self.panel,i))

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
        
    def 添加表头(self):
        for i in var.信息表[0] :
            temp =self.__创建label(i,150)
            self.grid_信息表.Add(temp, pos = (var.信息表[0].index(i),0), flag=wx.EXPAND )

    def 添加信息表(self, grid, panel):
        # 添加表格
        for i in var.单位列表:
            self.表.append([])
            temp= None
            temp = i.get信息()
            for j in range(len(temp)) :
                _l = self.__创建label(str(temp[j]),100 )
                self.表[-1].append(_l )
                _pos=( j, var.单位列表.index(i)+1)
                grid.Add(_l, pos = _pos, flag=wx.EXPAND )
            
    def 刷新(self,e):
        print('--'*20)
        print('--'*20)
        for i in var.单位列表:
            i.sub预算()

        for i in var.单位列表:
            temp= None
            temp = i.get信息()
            for j in range(len(temp)) :
                self.表[var.单位列表.index(i)][j].SetLabel(str(temp[j]))

    def 刷新2(self,e):
        print('--'*20)
        print('--'*20)
        for i in var.单位列表:

            i.sub结算()
        for i in var.单位列表:
            temp= None
            temp = i.get信息()
            for j in range(len(temp)) :
                self.表[var.单位列表.index(i)][j].SetLabel(str(temp[j]))


    def 菜单栏事件(self,event):
        id = event.GetId()
        if id == wx.ID_NEW: 
            self.Menu2.SetTitle(str(random.random())) #SetLabel(random.random())
        if id == 1099: 
            self.MenuItem1.SetTitle(str(random.random())) 
        #s=event.GetValue()
        print(event.GetEventObject().Title)

    def 添加资源栏(self, grid):
        # 添加表格
        for i in var.单位列表:
            i.addCtrls(self.panel)
            grid.Add( i.grid, 10,flag=wx.ALL|wx.EXPAND)



    def __创建label(self,txt='txt',宽度=50,字体=20,颜色='#FFFFFF'):
        temp = wx.StaticText(self.panel, label=txt,size=(宽度,-1),style=wx.ALIGN_CENTRE)
        temp.SetBackgroundColour(颜色)
        font = wx.Font(字体,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL) 
        temp.SetFont(font) 
        return temp


    def display(self, e=0):
        try:
            _thread.start_new_thread(self.刷新, ("Thread-1", 5, ))
        except:
            print("Error: 无法启动线程")

    def 预算(self):
        for i in var.单位列表:
            i.sub预算()
            print('buy',var.buy)
            print('out',var.out)



def 启动窗口():
    print('程序开始 ...')
    app = wx.App()
    #app.locale = wx.Locale(wx.LANGUAGE_CHINESE_SIMPLIFIED)
    win = Mywin()
    

    app.MainLoop()


启动窗口()






