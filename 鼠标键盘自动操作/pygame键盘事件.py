import logging
import sys
import threading
import time
from ctypes import *
from ctypes.wintypes import *
from sys import exit

import pyautogui
import pygame
from pygame.locals import *
from pynput.keyboard import Listener

#mouseDown()和mouseUp()函数可以实现鼠标按下和鼠标松开的操作。两者参数相同，有x，y和button。
# 鼠标移动到该位置单击左键
#pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
#放开鼠标
# 鼠标移动到该位置放开左键
# pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
gettime=lambda :time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def wait(t=10):
    for i in range(t):
        print('开始点击时间还有：{:>3d}'.format(t-i),'秒')
def log(ss):
    print(ss)





background_image_filename = 'sea.png'
#mouse_image_filename = 'C:/Users/bmzk1/Documents/GitHub/my_python_program/鼠标键盘自动操作/fish.png'
mouse_image_filename = 'fish.png'

if __name__ == "__main__":
    # 初始化pygame，为使用硬件做准备
    pygame.init()
    log('init')
    # 创建一个窗口
    screen = pygame.display.set_mode((640,480))
    # 设置窗口标题
    pygame.display.set_caption("hello,world!")
    log(screen)
    log('screen')


    # 加载图片并转换
    background = pygame.image.load(background_image_filename)
    #background = pygame.image.load(r'C:/Users/bmzk1/Documents/GitHub/my_python_program/鼠标键盘自动操作/sea.jpg')
    mouse_cursor = pygame.image.load(mouse_image_filename)


    delta = 0.3
    lastTime = 0

    WM_HOTKEY   = 0x0312
    MOD_ALT     = 0x0001
    MOD_CONTROL = 0x0002
    MOD_SHIFT   = 0x0004
    WM_KEYUP    = 0x0101
    class MSG(Structure):
        _fields_ = [('hwnd', c_int),
                    ('message', c_uint),
                    ('wParam', c_int),
                    ('lParam', c_int),
                    ('time', c_int),
                    ('pt', POINT)]
    key = 192 # ~ 键
    hotkeyId = 1
    if not windll.user32.RegisterHotKey(None, hotkeyId, None, key):
        sys.exit("Cant Register Hotkey")

    msg = MSG()





    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出时间后退出程序
                exit()
            if event.type == pygame.KEYUP:
                #time.sleep(3)
                #jt=jt*2
                #c.tick(jt)
                print("jt = ",time.time())
                wait()
        # 将背景图画上去
        screen.blit(background, (0, 0))

        # 获得鼠标位置
        x, y = pygame.mouse.get_pos()
        # 计算光标左上角位置
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2

        # 将光标画上去
        screen.blit(mouse_cursor, (x, y))

        # 刷新画面
        pygame.display.update()


        # c=pygame.time.Clock()
        # log(c.tick())
        # c.tick(1)
        # print('tick',c.tick())
        # t1=time.time()
        # t2=0
        # jt=1
        # while True:
        #     t1=t2
        #     t2=time.time()
        #     print(gettime(),'{:3f}'.format(t2-t1))
        #     #print('pygame.evet.get()')
        #     for event in pygame.event.get():
        #         # 判断用户是否点击了关闭按钮
        #         print(event)
        #         time.sleep(5)
        #         if event.type == pygame.KEYUP:
        #             #time.sleep(3)
        #             jt=jt*2
        #             c.tick(jt)
        #             print("jt = ",jt)
        #             wait()
        #         if event.type == pygame.KEYDOWN:
        #             jt=jt*0.5
        #             c.tick(jt)
        #             print("jt = ",jt)
        #             wait()

        if (windll.user32.GetMessageA(byref(msg), None, 0, 0) != 0):
            if msg.message == WM_HOTKEY and msg.wParam == hotkeyId:
                if (time.time() - lastTime) < delta:
                    print ("down")
                else:
                    pass
                lastTime = time.time()
            if msg.message == WM_KEYUP:
                print ("up")
            windll.user32.TranslateMessage(byref(msg))
            windll.user32.DispatchMessageA(byref(msg))





    pygame.quit()
def gt():
    t=(time.time()-1566439000)






def click(n=1,t=1):
    '''鼠标点击 n 次,间隔 t 秒'''
    for i in range(n):
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        #pyautogui.click( clicks=1, interval=t, button='left')
        time.sleep(t)
        print('{:>3d}'.format(i+1),gettime())
        



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
