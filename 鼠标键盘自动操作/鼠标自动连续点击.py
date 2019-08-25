import threading
import time
import pyautogui
import pyperclip

# #  鼠标向下移动10像素
# pyautogui.moveRel(None, 10)
# pyautogui.doubleClick()
# #  用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
# #  use tweening/easing function to move mouse over 2 seconds.
# pyautogui.moveTo(1800, 500, duration=2, tween=pyautogui.easeInOutQuad)
# #  在每次输入之间暂停0.25秒
# pyautogui.typewrite('Hello world!', interval=0.25)
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#pyperclip.copy('中文')  # 先复制
#pyautogui.hotkey('ctrl', 'v')  # 再粘贴

#mouseDown()和mouseUp()函数可以实现鼠标按下和鼠标松开的操作。两者参数相同，有x，y和button。
# 鼠标移动到该位置单击左键
#pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
#放开鼠标
# 鼠标移动到该位置放开左键
# pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')



def gt():
    t=(time.time()-1566439000)

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
import logging

wenjianweizhi = "D:\\hi\\"

logging.basicConfig(filename=(wenjianweizhi+"keylogger.txt"),format="%(asctime)s:%(message)s",level=logging.DEBUG)
print('log')
def press(key):
    logging.info(key)
    a=key
    print('按下了',key,str(key))
 

print('def')

def display(t=10):
    for i in range(100000):
        print('{:>4d}'.format(i),'t=','{:>3d}'.format(t))
        time.sleep(a*0.1)
a=100
print(a,type(a))
display(a)
wait(t=10)
#click(10000,0.2)
print('with')
with Listener(on_press = press) as listener:
        listener.join()
