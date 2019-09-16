import wx
import time

import threading

def timestr():
    '''获取指定格式的时间'''
    rv=time.strftime("%H:%M:%S", time.localtime()) 
    rv=rv+'::'+str(int((time.time()-int(time.time()))*1000))
    return rv

class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''
    def __init__(self):
        ''' 构造函数'''
        super(Mywin, self).__init__(None, title='Dota2 游戏数据修改', size=(600, 400))
        ############################################################
        self.grid = wx.BoxSizer(wx.VERTICAL) 
        self.panel = wx.Panel(self)
        ###########################################################
        print('# self.Show()')
        self.addctrls(self.panel,self.grid)
        

        self.isshurtdowning=False

        print('end')
        self.timer1 = threading.Timer(1,self.timerdef)
        self.timer = threading.Timer(1,self.timerdef)
        self.nnn=0
        self.lasttime=300
        self.endtime=1568625000
        
        print(1)
        self.panel.SetSizerAndFit(self.grid)
        print(2)
        self.Center()
        print(3)
        self.timerdef(0.02)
        self.Show()
    def addctrls(self,panel,grid):
        self.addbox1( panel,grid)
        self.fgx()
        ##############################################################
        self.endtime_label=wx.StaticText(self.panel,style=wx.ALIGN_CENTER,label='fsd')
        self.endtime_label.SetForegroundColour(wx.RED)
        self.endtime_label.SetBackgroundColour(wx.BLACK)
        font = wx.Font(35, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.NORMAL) 
        self.endtime_label.SetFont(font)
        self.grid.Add(self.endtime_label,flag=wx.CENTER)
        self.fgx()
        #####################################
        self.addbox2( panel,grid)
        self.fgx(3)
        #########################################
        self.addbox3( panel,grid)
        self.fgx()
        #########################################
        self.addbox4( panel,grid)
        self.fgx()

    def addbox1(self, panel,grid):
        '''窗口第一行，显示模式选择和本地时间'''
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.NORMAL) 
        # 容器
        self.box1=wx.BoxSizer(wx.HORIZONTAL)
        # 控件1
        self.rb1 = wx.RadioButton(panel,label = '倒计时模式') 
        self.rb1.SetFont(font)
        self.box1.Add(self.rb1)
        # 控件2
        self.rb2 = wx.RadioButton(panel,label = '定时模式') 
        self.rb2.SetFont(font)
        self.box1.Add(self.rb2)
        # 控件3
        w=wx.StaticText(panel)
        #w.SetBackgroundColour(wx.BLACK)
        self.box1.Add(w,1,flag=wx.ALL|wx.EXPAND)
        # 控件4
        label_localtime = wx.StaticText(panel,label = '本地时间：') 
        label_localtime.SetFont(font)
        self.box1.Add(label_localtime)
        # 控件5
        self.localtime = wx.StaticText(panel,label = time.strftime("%H:%M:%S", time.localtime())) 
        self.localtime.SetFont(font)
        self.localtime.SetBackgroundColour((200,200,200))
        #localtime.SetForegroundColour((100,0,0)) 
        self.box1.Add(self.localtime)
        # 控件6
        font2 = wx.Font(12, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.NORMAL) 
        self.localtime2 = wx.StaticText(panel,label = '::'+str(int((time.time()-int(time.time()))*1000)))
        self.localtime2.SetFont(font2)
        self.localtime2.SetBackgroundColour((200,200,200))
        self.localtime2.SetForegroundColour((255,0,0)) 
        self.box1.Add(self.localtime2)
        # 添加到面板
        grid.Add(self.box1,flag=wx.EXPAND)

    def addbox2(self, panel,grid):
        self.box2=wx.BoxSizer(wx.HORIZONTAL)
        self.box2.Add(wx.StaticText(panel),1,flag=wx.EXPAND)
        self.h=t(panel,self.box2)
        self.m=t(panel,self.box2)
        self.s=t(panel,self.box2)
        self.box2.Add(wx.StaticText(panel),1,flag=wx.EXPAND)
        grid.Add(self.box2,flag=wx.EXPAND)

    def addbox3(self, panel,grid):
        self.gauge=wx.Gauge(panel)
        self.gauge.BackgroundColour=wx.BLACK
        self.gauge.ForegroundColour=wx.RED
        self.gauge.Value=50
        grid.Add(self.gauge,flag=wx.EXPAND)

        self.gauge_label=wx.StaticText(self.panel,label='20/100',style=wx.ALIGN_CENTER)
        #self.gauge_label.SetBackgroundColour(colour=wx.BLUE)
        #self.gauge_label.SetPosition((self.Size[0]*0.5,self.gauge.GetPosition()[1]))
        grid.Add(self.gauge_label,flag=wx.EXPAND)

    def addbox4(self, panel,grid):
        font2 = wx.Font(30, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.bt=wx.Button(panel,label='开 始',size=(250,80))
        self.bt.SetFont(font2)
        grid.Add(self.bt,flag=wx.CENTER)
        self.bt.Bind(wx.EVT_BUTTON, self.bindingevent_bt) 

    def fgx(self,n:'权重'=10):
        '''分割线'''
        st=wx.StaticText(self.panel)
        #st1.SetBackgroundColour(colour=wx.YELLOW)
        self.grid.Add(st,1,flag=wx.EXPAND)

    def bindingevent_bt(self,event):
        if self.bt.Label=='开 始':
            self.isshurtdowning=True
            self.bt.Label='暂 停'
        else:
            self.isshurtdowning=False
            self.bt.Label='开 始'
        

    def shutdown(self):
        print('shutdown')
        pass
    
    def timerdef(self,intever=0.2):
        self.timer = threading.Timer(intever,self.timerdef)
        self.timer.start()

        self.nnn=self.nnn+1
        print(self.nnn,threading.activeCount())
        self.localtime.Label=time.strftime("%H:%M:%S", time.localtime())
        self.localtime2.Label = '::'+self.int_str((time.time()-int(time.time()))*100)
        
        h=time.localtime(self.endtime-time.time())[3]
        m=time.localtime(self.endtime-time.time())[4]
        s=time.localtime(self.endtime-time.time())[5]
        self.h.st.Label=self.int_str(h)+'时'
        self.m.st.Label=self.int_str(m)+'分'
        self.s.st.Label=self.int_str(s)+'秒'

        self.endtime_label.Label='关机时间：'+time.strftime("%H:%M:%S", time.localtime(self.endtime))
        if self.endtime<time.time():
            self.shutdown()
    def int_str(self,n):
        n=int(n)
        if n<10:
            rv='0'+str(n)
        else:
            rv=str(n)
        return rv



class t(object):
    def __init__(self,panel,grid):
        sizer=wx.GridBagSizer()

        font1 = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.st=wx.StaticText(panel,style=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT,label='99面',size=(130,30))
        self.st.SetFont(font1)
        self.st.SetBackgroundColour((220,220,220))
        sizer.Add(self.st,pos=(0,0),span=(2,1),flag=wx.EXPAND)

        font2 = wx.Font(25, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.bt_up=wx.Button(panel,label='+',size=(30,30))
        self.bt_up.SetFont(font2)
        sizer.Add(self.bt_up,pos=(0,1))
        
        self.bt_down=wx.Button(panel,label='-',size=(30,30))
        self.bt_down.SetFont(font2)
        sizer.Add(self.bt_down,pos=(1,1))

        grid.Add(sizer)

def 启动窗口():
    app = wx.App()
    win = Mywin()
    app.MainLoop()

启动窗口()