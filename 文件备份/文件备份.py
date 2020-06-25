#encoding=utf-8

import win32serviceutil 
import win32service 
import win32event 

import threading
import time
class PythonService(win32serviceutil.ServiceFramework): 
    #服务名
    _svc_name_ = "PythonService"
    #服务在windows系统中显示的名称
    _svc_display_name_ = "Python Service 文件备份"
    #服务的描述
    _svc_description_ = "付鹏程 文件备份 服务"
 
    def __init__(self, args): 
        win32serviceutil.ServiceFramework.__init__(self, args) 
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def tick_sub(self):
        tstr = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        print(time.time(),tstr)

    def SvcDoRun(self):
        # 把自己的代码放到这里，就OK
        start_time=time.time()
        timer = threading.Timer(5, self.tick_sub)
        # 等待服务被停止 
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE) 
            
    def SvcStop(self): 
        # 先告诉SCM停止这个过程 
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) 
        # 设置事件 
        win32event.SetEvent(self.hWaitStop) 
 
if __name__=='__main__': 
    win32serviceutil.HandleCommandLine(PythonService)  
    #括号里参数可以改成其他名字，但是必须与class类名一致；


#python 文件备份.py start




