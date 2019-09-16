'''给定3个点和P点到这3个点的距离,求出P点的坐标'''



class point(object):
    def __init__(self,x=0,y=0,z=0,d=100,v=0):
        self.x=x
        self.y=y
        self.z=z
        self.d=d
    def k(self):
        return self.d**2-self.x**2-self.y**2-self.z**2





import math
import random


def caluate(x2,x3,y3,d1,d2,d3,v):
    p1=point()
    p2=point(x2)
    p3=point(x3,y3)
    x=0.5*(p1.k()-p2.k())/p2.x
    y=(p1.k()-p3.k())*p2.x+(p1.k()-p2.k())*p3.x/2/p2.x/p3.y
    z=math.sqrt(p1.d**2-p1.x**2-p1.y**2)
    rv=point(x,y,z)
    return rv




def mainsub(x2,x3,y3,tp:point,v):
    '''tp: true point'''
    p1=point()
    p2=point(x2)
    p3=point(x3,y3)
    d=lambda p:math.sqrt((tp.x-p.x)**2+(tp.y-p.y)**2+(tp.z-p.z)**2)+v
    k=lambda p:d(p)**2-p.x**2-p.y**2-p.z**2
    x = (k(p1)-k(p2))/2/x2
    y = (k(p1)*x2-k(p3)*x2-k(p1)*x3+k(p2)*x3) /2/x2/y3
    #print(tp.x,tp.y,tp.z)
    #print(d(p1)**2-x**2-y**2,x,y)
    try:
        z=math.sqrt(d(p1)**2-x**2-y**2)
    except :
        z=0
        print('error ',tp.x,tp.y,x,y)
    rv=point(round(x,3),round(y,3),round(z,3),round(d(point(x,y,z)),3))
    return rv 

dlist=[]
n=1000*10000*1
for i in range(1,n):
    r=lambda a=6,b=8:random.randint(10**a,10**b)
    x2=100#r()*math.sin(r())
    x3=50#r()*math.sin(r())
    y3=50#r()*math.sin(r())
    tp=point(r(),r(),r())
    v=1 #random.randint(2,2000)*(math.sin(r())-0.5)*0.001
    p=mainsub(x2,x3,y3,tp,v)
    dx='{:+.3f}'.format(p.x-tp.x).rjust(8)
    dy='{:+.3f}'.format(p.y-tp.y).rjust(8)
    dz='{:+.3f}'.format(p.z-tp.z).rjust(8)
    #d ='{:+.3f}'.format(math.sqrt((p.x-tp.x)**2+(p.y-tp.y)**2+(p.z-tp.z)**2))
    dlist.append(math.sqrt((p.x-tp.x)**2+(p.y-tp.y)**2+(p.z-tp.z)**2))
    #print('i =','{:3d}'.format(i),'v=','{:+.3f}'.format(v).rjust(8),dx,dy,dz,d)
    if i%10000 == 0:
        print('i =','{:3d}'.format(i),)
        dlist.sort()
        s=int(math.sqrt(tp.x**2+tp.y**2+tp.z**2))
        for j in range(int(i*0.95),int(i*0.95)+20):
            print('{:8d}'.format(j),'{:+.6f}'.format(dlist[j]),'{:+.6f}'.format(max(dlist))
            ,'{:,}'.format(s)
            )