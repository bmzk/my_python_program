
import os
import time


print(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()) )
ts=0
print('请输入多少分钟后关机:')
while ts<180 :
    try :
        tm=float(input('请输入 1 个大于 3 的数字:'))
        ts=int(tm*60)
    except :
        print('输入错误,请输入 数字')
        pass


while ts>0:
    ts = ts-1
    if ts >60 :
        print(ts//60,'分',ts%60,'秒','后关机...')
    else :
        print(ts,'秒后关机...')
    time.sleep(1)

os.system('C:\\Windows\\System32\\shutdown.exe -s -t 1')

