import time
import os


def getTime():
    t_current=time.time()
    t=time.localtime(t_current)
    ms=int((t_current-int(t_current))*1000)
    ps=int((t_current-int(t_current))*(10**6))%1000
    returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms).rjust(3,'0')
    #returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms)+':::'+str(ps)
    return returnValue
	
a=True
print('start')
i=1
while i>0:
    #os.system('cls')              
    print(str(i).rjust(5),getTime())
    i+=1
print('end')
