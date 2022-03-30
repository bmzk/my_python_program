'''鼠标自动在屏幕指定坐标点击'''
import pyautogui
# pyautogui.click(x,y,clicks,interval,duration)
# clicks: 点击次数，默认1次。次数为2，等于一次双击操作
# interval: 两次点击间隔时长，默认0.0；大于1.0后。默认为点击一次
# duration: 所耗时长，默认0.0。


x = 1757
y = 1048
# 点击次数
n = 10
# 点击间隔，秒
t = 0.5

for i in range(n):
    pyautogui.click(x, y, clicks=1, interval=t)
    print('第 %d/%d 次点击 ...'%(i, n))
