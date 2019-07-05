import threading
import time

import pyautogui
import pyperclip
import 名单
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


#pyperclip.copy('中文')  # 先复制
#pyautogui.hotkey('ctrl', 'v')  # 再粘贴
t=lambda :time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

h1=[1725,405] #id
h2=[1725,430]  #name
h3=485  #enter
h4=460  #return
def 截图():
    '''1秒后截图，然后再等待2秒'''
    print(t(),'1秒后截图')
    time.sleep(1)
    pyautogui.press('printscreen')
    print(t(),'等待 2秒')
    time.sleep(1)

def f(id,name):
    print('--'*9)
    #input id
    pyautogui.moveTo(h1[0],h1[1]  , duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    for ii in range(15):
        pyautogui.press('backspace')
    pyautogui.typewrite(id, interval=0.1)

    #input name
    pyautogui.moveTo(h2[0],h2[1]  , duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    for i in range(10):
        pyautogui.press('backspace')
    pyperclip.copy(name)  # 先复制
    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
    #enter
    pyautogui.moveTo(1630,h3  , duration=1, tween=pyautogui.easeInOutQuad)
    截图()
    pyautogui.click()#
    #return
    pyautogui.moveTo(1460,h4  , duration=1, tween=pyautogui.easeInOutQuad)
    截图()
    pyautogui.click()
    #print('sleep...1 s')


def w(*mystr):
    file='C:\\Users\\asd\\Desktop\\log.txt'
    wf=open(file,'a')
    wf.write(str(mystr) +'\n')
    wf.close()

n=15
mylist=list(名单.d.values())
kc=['012','142','157','143','041','194']
l2=['00','01','02','03']
#for j in range(n,len(d)):
j=10
for i in kc:
    for k in l2:
        id=mylist[j][0].replace('*****',i+k)
        name=mylist[j][1]
        print(t(),i,j,id,name)
        f(id,name)
        #input('.....')
        w(time.localtime(time.clock()),i,j,id,name)

print (t())
