
import time
import os


def getTime(f=0):
    t_current = time.time()
    t = time.localtime(t_current)
    ms = int((t_current-int(t_current))*1000)
    ps = int((t_current-int(t_current))*(10**6)) % 1000

    if f==0:
        returnValue = time.strftime('%Y/%m/%d %H:%M:%S', t)+'::'+str(ms).rjust(3, '0')
    elif f==1:
        returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms)+':::'+str(ps)
    elif f==2:
        returnValue=time.strftime('%Y%m%d-%H%M%S',t)
    return returnValue



if __name__=='__main__':
    print(getTime(2))