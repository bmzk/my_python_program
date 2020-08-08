
import time
import pyautogui


gettime=lambda :time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def wait(t=10):
    for i in range(t):
        print('开始点击时间还有：{:>3d}'.format(t-i),'秒')

def click(n=1,t=1):
    '''鼠标点击 n 次,间隔 t 秒'''
    for i in range(n):
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        #pyautogui.click( clicks=1, interval=t, button='left')
        time.sleep(t)
        print('{:>3d}'.format(i+1),gettime())

from pynput.keyboard import Listener

def press(key):
    a=key
    print('按下了',key,str(key))
 

wait(t=10)
#click(10000,0.2)
print('with')
with Listener(on_press = press) as listener:
        listener.join()
