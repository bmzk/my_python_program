if __name__=='__main__':
    print('这是一个产生随机数的模块,不应该直接被运行')
    for i in range(3):
        print('--'*20)
import math
import time
def getRnd(count=10,averageValue=0.0,maxRnd=10,minRnd=-10,n=2,rnd_f=lambda i,x=5:math.sin(time.time()+i+x)):
    '''产生一组随机数,
    count:随机数数量,uint
    averageValue:平均值,float
    maxRnd -minRnd:最大最小值之差,float
    n:保留的小数位数
    rnd_f:初始随机数生成函数,每次运行产生一个随机数'''
    '''思路:先产生一组随机数,再平移至制定平均值位置,最后缩放'''
    def __检查输入参数错误 ():
        if minRnd>=maxRnd:
            print('minRnd >=  maxRnd')
            print('设定 minRnd =',  maxRnd-2)
            print('--'*25)
        if count <1:
            print('count输入错误,设定 count = 10',)
    #1 产生一组随机数
    v=[]
    for i in range(count):
        v.append(rnd_f(i))
    #2 平移
    average=round(sum(v)/count ,n)
    #print(v)
    for i in range(count):
        v[i]+=averageValue-average
    #print(v)
    #3 缩放
    vmax=max(v)
    vmin=min(v)
    for i in v:
        if maxRnd/(vmax-averageValue)<=minRnd/(vmin-averageValue):
            v[v.index(i)]=(i-averageValue)*maxRnd/(vmax-averageValue)+averageValue
        else:
            v[v.index(i)]=(i-averageValue)*minRnd/(vmin-averageValue)+averageValue
    #4 修整
    for i in range(count):
        v[i]=round(v[i],n)
    #print(v)

    余数=sum(v)-averageValue*count
    for i in v:
        if i-余数<=maxRnd and i-余数>=minRnd:
            #print(1,'余数=',余数,i)
            #print(sum(v),v,i)
            v[v.index(i)]=i-余数
            #print(sum(v),v,i)
            余数=0
            break
        elif i-余数>maxRnd:
            余数=余数+(maxRnd- v[v.index(i)])
            v[v.index(i)]=maxRnd
            break
        else:
            余数=余数-( i-minRnd)
            v[v.index(i)]=minRnd
            break
    for i in range(count):
        v[i]=round(v[i],n)
    return v
