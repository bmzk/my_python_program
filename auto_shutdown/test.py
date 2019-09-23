import math
import os
import threading
import time
import winsound

import wx


def timestr():
    '''获取指定格式的时间'''
    rv=time.strftime("%H:%M:%S", time.localtime()) 
    rv=rv+'::'+str(int((time.time()-int(time.time()))*1000))
    return rv

class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''
    def __init__(self):
        ''' 构造函数'''
        super(Mywin, self).__init__(None, title='自动关机', size=(600, 400))
        ############################################################
        self.grid = wx.BoxSizer(wx.VERTICAL) 
        self.panel = wx.Panel(self)
        ###########################################################
        self.addctrls(self.panel,self.grid)
        print('end')
        self.timer=wx.Timer(self)
        self.timer.Start(50,False)

        self.lasttime=0
        self.endtime=time.time()+5000
        
        print(1)
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        self.Show()


    def addctrls(self,panel,grid):
        # 控件5
        self.time1 = wx.StaticText(panel,label = time.strftime("%H:%M:%S", time.localtime())) 
        grid.Add(self.time1,1,flag=wx.EXPAND)
        # 控件6
        self.time2 = wx.StaticText(panel,label = '::'+str(int((time.time()-int(time.time()))*1000)))
        grid.Add(self.time2,1,flag=wx.EXPAND)
        # 绑定事件
        self.Bind(wx.EVT_TIMER, self.OnTimer1Event)

    def bingevent_bt_use(self,k=1,n=3600):
        '''k：点击向上按钮k=1，点击向下按钮k=-1\n
        n：每次点击增加或减少的数值'''
        if self.rb1.Value:
            self.lasttime += k*n
            self.endtime=self.lasttime+time.time()
        elif self.rb2.Value:
            self.endtime += k*n
        if self.lasttime < 0:
            self.lasttime = 0
        #
        self.gauge.SetRange(self.lasttime)
        # 发声音
        f=int(math.log10(n))*500+500+k*100
        print(f)
        winsound.Beep(f,200)

    def OnTimer1Event(self,event):
        print('Timer1Event...')
        self.time1.Label=time.strftime("%H:%M:%S", time.localtime())
        self.time2.Label = '::'+str((time.time()-int(time.time()))*100)




def 启动窗口():
    app = wx.App()
    win = Mywin()
    app.MainLoop()

启动窗口()
