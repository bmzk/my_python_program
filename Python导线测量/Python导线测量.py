import random
import 函数.改正数
import 函数.随机数
import 函数.类定义
import copy
import math
import time
import turtle
from 函数.函数 import log



def display():
    def play(str,obj):
        for i in obj:
            print(str,i)

    log('程序日志,用于检查bug',l_c_r='l')
    log(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))#"%Y年%m月%d日",
    log('----'*10,l_c_r='l')
    test=函数.类定义.导线测量题目(example_ID,example_n,example_B,example_A,导线全长相对闭合差限差_倒数)
    log('第 ',example_ID,' 题')
    log(test.坐标增量闭合差.tostring2,'角度闭合差=',test.角度闭合差)   
    log('观测角度','角度观测值','改正数','改正后角度','方位角',width=12)
    for i in  range(example_n+1):
        try:
            log(test.角度观测值[i].name,test.角度观测值[i].tostring(),test.角度改正数[i],test.改正后角度[i].tostring() 
            ,test.方位角[i].name,test.方位角[i].tostring(),width=15)
        except IndexError:
            log('IndexError    i=',i)
        except:
            pass

        
    log('坐标增量闭合差',test.坐标增量闭合差.tostring2())
    log('      导线平均边长','坐标增量(x,y)','  改正数(x,y)','     改正后坐标增量(x,y)','   导线点',width=15)
    for i in  range(example_n+1):
        log(test.导线边观测值平均数[i].tostring(5),test.坐标增量[i].tostring2(),test.坐标增量改正数[i].tostring2(),
            test.改正后坐标增量[i].tostring2(),test.导线点[i].tostring(),width=20)
    log()   
    for i in range(1,example_n+2):
        #print(test.导线点[i].tostring())
        bob.goto(test.导线点[i].y/500,test.导线点[i].x/500)


'''初始定义'''
#公共变量
example_ID =random.randint(0,9)  #题号,代表第几题
example_l=100000 #导线平均边长,单位毫米
example_n  =4 # random.randint(3,10)#导线边数量
example_A =函数.类定义.点('p1',0,00)
j_max=int(16*math.sqrt(example_n))     #角度闭合差限差
导线全长相对闭合差限差_倒数=10000       #导线全长相对闭合差限差
example_B=函数.类定义.点('p0',0,0)#后视定向函数.类定义.点

bob=turtle.Turtle()

print('---'*9)
for i in range(9999):
    example_ID=i
    example_n=4
    #input('输入导线边个数')
    bob.clear()   
    bob.pendown
    display()
    bob.penup

print('---'*9)









class asd (object):
    def __init__(self, long=5.5, **kwargs):
        self.l=long
        return None
k=[]
for i in range(9):
    example_ID=i
    k.append(asd(random.randint(-5,5)))
    print(k[i          ].l)
    
print(k)
print(sum(i.l for i in k))



