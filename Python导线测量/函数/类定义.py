import 函数.随机数
import 函数.函数
import math


class 点(object):
    '''点类型定义'''
    def __init__(self, 点名:str, x坐标:int,y坐标:int):
        self.name=点名
        self.x=x坐标
        self.y=y坐标
        return None
    def tostring(self):
        '''包含点名,形式为 name:(x,y)'''
        return self.name+': ('+str(self.x/1000)+","+str(self.y/1000)+")"
    def tostring2(self):
        '''不包含点名,形式为 (x,y)'''
        return '('+str(self.x/1000)+","+str(self.y/1000)+")"
class 边(object):
    def __init__(self, 长度:int, 名字:str):
        self.l=长度
        self.name=名字
        return None
    def  tostring(self,width=20):
        return ('边名:'+self.name).center(width)    +('长度='+str(self.l/1000)).center(width)
class 角(object):
    '''角度的类
    s_total:    以秒计算的角度,int
    r:  以弧度计算的角度,float
    d:  度 ,int
    m:  分,int
    s:  秒,int
    tostring:   string,以**度**分**秒形式输入
    '''
    def __init__(self, 以秒记的角度):           
        self.s_total=round(以秒记的角度)
        if self.s_total==360*3600:
            self.s_total=0
        return None
    r=lambda self:math.radians(self.s_total/3600.0)
    #d=lambda self:int(self.s_total/3600)
    def d(self):
        #print(0,self.s_total)
        return int(self.s_total/3600)
    m=lambda self:int(self.s_total/60)-self.d()*60
    s=lambda self:self.s_total % 60
    tostring=lambda self:str(self.d())+'度'+str(self.m())+'分'+str(self.s())+'秒'

class 导线测量题目(object) :
    '''
    p:导线点集合,p[0]为后视定向点
    e:元祖,误差点,x为x增量闭合差,y为y增量闭合差
    d:导线边长列表第0个为后视定向边
    改正后角度:导线角度列表,第0个为看后视点角
    方位角:各条边的原始坐标方位角
    d_total:    导线全长
    角度闭合差:角度闭合差

    '''
    #函数定义
    def __getd(self,p1,p2): 
        '''计算两点之间的距离'''
        b=边(round(math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)),"")
        b.name=p1.name+p2.name
        return b
    def __getj(self,fwj1,fwj2):#左侧点,测站点,右侧点
        '''根据两条直线的方位角计算直线夹角(左角)'''
        v=角(fwj2.s_total-fwj1.s_total)
        if v.s_total>=180*3600:
            v.s_total-=180*3600
        else:
            v.s_total+=180*3600
        v.name=fwj1.name[:2]+fwj2.name
        return v
    def __getfwj(self,p1,p2):
        '''计算直线方位角,
        fwj:坐标方位角,以 整数秒来表示'''
        fwj=角(0)
        fwj.name=p1.name+p2.name
        dy=p2.y-p1.y
        dx=p2.x-p1.x

        if dx==0:
            fwj.s_total=90*3600
        else:
            fwj.s_total=round (math.degrees(math.atan(dy/dx))*3600)
            #log('fwj.s_total',fwj.s_total,fwj.tostring(),fwj.s())
        if dx>0:
            if dy>0:
                pass
            else:
                fwj.s_total+=360*3600
        else:
            fwj.s_total+=180*3600
        #log('dx',dx,'dy',dy,'fwj',fwj.tostring)
        if fwj.s_total==360*3600:
            fwj.s_total=0
        return fwj

    def __创造基础数据(self):
        '''创造基础数据:创造导线点
        思路:假定导线点均匀分布在一个半径为 r 的椭圆上面,圆心为原点,第一个点在最上方(加初始偏转角度),逆时针方向数
        椭圆方程:(x/a)**2+(y/b)**2=1  ,又有  sin**2+cos**2=1,所以x=a*cos,y=b*sin
        self.__n:导线点数,int
        l:导线平均边长,int,单位为毫米
        p:导线点的集合,每个点是一个字典,例如{'x':50,'y':50}
        r:圆的半径
        ja:每个导线边所所对应的圆心角
        '''
        rnd=函数.随机数.getRnd(count=self.__n,averageValue=math.pi*2/self.__n,maxRnd=math.pi*4/self.__n,minRnd=math.pi/self.__n
                          ,n=5,rnd_f=lambda x:math.sin(x+self.__ID))
        #print('+++',rnd)
        a=100000+50000*math.sin(self.__ID*0.3)
        b=100000+50000*math.cos(self.__ID*0.3)
        p=[]
        p.append(self.__后视点)
        ja=0
        x=0
        y=0
        for i in range(self.__n):
            ja+=rnd[i]
            x=round(a*math.cos(ja))
            y=round(b*math.sin(ja))
            p.append(函数.类定义.点('p'+str(i+1),x,y))
            #print(123456,p[i].x)
        p.append(p[1])
        offset=函数.类定义.点('平移量',p[1].x,p[1].y)
        #print(offset.tostring())
        for i in range(1,len(p)-1):
            #print(i,offset.x,p[i].x)
            p[i].x+=self.__第一点.x*1000-offset.x
            #print(i,offset.x,p[i].x)
            p[i].y+=self.__第一点.y*1000-offset.y
        return p
    def __角度部分计算(self):
        '''导线测量计算表中角度部分的计算:  
        角度观测值>>改正数>>改正后角度>>坐标方位角的计算'''
        for i in range(self.__n):
            self.方位角.append(self.__getfwj(self.导线点[i],self.导线点[i+1]))
            #log('方位角'+str(i)+' = ',self.__getfwj(p[i],p[i+1]).tostring())
        self.方位角.append(self.__getfwj(self.导线点[self.__n],self.导线点[1]))

        for i in range(self.__n):
            self.改正后角度.append(self.__getj(self.方位角[i],self.方位角[i+1]))
        self.改正后角度.append(self.__getj(self.方位角[self.__n],self.方位角[1])) #列表中角度顺序为O-B-C-D-A

        self.角度闭合差=int(math.sin(self.__ID)*math.sqrt(self.__n)*0.5)
        self.角度改正数=函数.改正数.计算角度改正数( self.改正后角度[1:self.__n+1],self.角度闭合差)
        
        self.角度观测值.append(self.改正后角度[0])
        for i in range(self.__n):            
            self.角度观测值.append(角(self.改正后角度[i+1].s_total-self.角度改正数[i+1]))
            self.角度观测值[i+1].name=self.改正后角度[i+1].name
        self.实测内角和=self.角度闭合差+(self.__n-2)*180*3600
        '''--------------------------------------------------------------------------'''
    def __坐标部分计算(self):
        '''导线测量计算表中坐标部分的计算:  
        边长>>坐标增量>>改正数>>改正后坐标增量'''
        #1 计算改正后导线边长
        for i in range(self.__n):
            self.改正后导线边长.append(self.__getd(self.导线点[i],self.导线点[i+1]))
        self.改正后导线边长.append(self.__getd(self.导线点[self.__n],self.导线点[1]))
        #2 计算 改正后坐标增量       
        for i in range(self.__n+1):
            x3=round(self.改正后导线边长[i].l*math.cos(self.方位角[i].r()))
            y3=round(self.改正后导线边长[i].l*math.sin(self.方位角[i].r()))
            self.改正后坐标增量.append(点(点名='p'+str(i)+'p'+str(i+1),x坐标=x3,y坐标=y3))
        #2 计算 坐标增量闭合差
        try:
                    r=sum(i.l for i in self.改正后导线边长)/self.导线全长相对闭合差['倒数']
        except ZeroDivisionError:
            print("导线全长相对闭合差['倒数'] = 0",'导线全长相对闭合差=',self.导线全长相对闭合差,'导线全长相对闭合差_限差倒数=',self.__导线全长相对闭合差_限差倒数)
        except:
            print('其他错误',self.导线全长相对闭合差,'导线全长相对闭合差_限差倒数=',self.__导线全长相对闭合差_限差倒数)
        print(self.导线全长相对闭合差,self.__导线全长相对闭合差_限差倒数)

        self.坐标增量闭合差=点('坐标增量闭合差',x坐标=round(r*math.cos(self.__ID*2)),y坐标=round(r*math.sin(self.__ID*2)))
        函数.函数.log(r,self.坐标增量闭合差.tostring())
        #3 计算 坐标增量改正数 
        x2=函数.改正数.计算坐标增量(self.改正后导线边长,self.坐标增量闭合差.x)
        y2=函数.改正数.计算坐标增量(self.改正后导线边长,self.坐标增量闭合差.y)
        for i in range(self.__n+1):
            self.坐标增量改正数.append(点(点名='p'+str(i)+'p'+str(i+1),x坐标=x2[i],y坐标=y2[i]))
        #4 计算 坐标增量 
        for i in range(self.__n+1):
            x1=self.改正后坐标增量[i].x-self.坐标增量改正数[i].x
            y1=self.改正后坐标增量[i].y-self.坐标增量改正数[i].y
            self.坐标增量.append(点(点名='p'+str(i)+'p'+str(i+1),x坐标=x1,y坐标=y1))

        for i in range(self.__n+1):
            self.导线边观测值平均数.append(self.__getd(self.导线点[i],self.导线点[i+1]))
    def __生成距离观测读数(self):
        pass
    def __生成角度观测读数(self):
        pass
   

    def __init__(self,myID=1,导线边数=4,后视点=点('后视点',x坐标=0,y坐标=0),第一点=点('p1',x坐标=500,y坐标=500)
                 ,导线全长相对闭合差_限差倒数=10000):
        self.__ID=myID    #题号
        self.__n=导线边数
        self.__后视点=点(后视点.name,后视点.x,后视点.y)
        self.__第一点=点(第一点.name,第一点.x*1000,第一点.y*1000)
        self.__导线全长相对闭合差_限差倒数=导线全长相对闭合差_限差倒数
        if self.__ID==0:
            self.__ID=1
        print('类初始化,创建类的实例')
        self.导线点=self.__创造基础数据()#真导线点,也就是最后要计算出来的点的坐标
        '''--------------------------------------------------------------------------'''
        '''角度部分'''
        '''--------------------------------------------------------------------------'''
        self.方位角=[] #元素为class jd
        self.改正后角度=[] #元素为class jd
        self.角度改正数=[]        
        self.角度观测值=[] #元素为class jd
        self.实测内角和=0
        self.角度闭合差=0
        self.__角度部分计算()
        self.角度观测读数=self.__生成角度观测读数()
        '''--------------------------------------------------------------------------'''
        '''坐标部分'''
        '''--------------------------------------------------------------------------'''
        self.导线点坐标=[]       
        self.改正后导线边长=[]#改正后导线边长
        try:
            self.导线全长相对闭合差={'value':'1/'+str(int(abs(math.sin(self.__ID))*self.__导线全长相对闭合差_限差倒数)),
                            '倒数':int((abs(math.sin(self.__ID)*0.5)+0.5)*self.__导线全长相对闭合差_限差倒数)}
        except:
            print(self.__ID,math.sin(self.__ID))
            raise
        #r=sum(i.l for i in self.改正后导线边长)*self.导线全长相对闭合差['value']
        #self.坐标增量闭合差=点('坐标增量闭合差',x坐标=round(r*math.cos(self.__ID*2)),y坐标=round(r*math.sin(self.__ID*2)))
        #log(r,self.坐标增量闭合差.tostring())
        self.改正后坐标增量=[]
        self.坐标增量改正数=[]
        self.坐标增量=[]
        self.导线边观测值平均数=[]
        self.__坐标部分计算()
        self.距离观测读数=self.__生成距离观测读数()
