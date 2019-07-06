import os
import random

f=open('C:\\Users\\asd\\Desktop\\20190701.txt','w+')
f2=open('C:\\Users\\asd\\Desktop\\20190701-2.txt','w+')
def w(*mystr):
    for i in mystr:
        f.write(str(i))
    f.write('\n')

#v=[0,0,0,0,0,0,0,0]
# def test(a=1):
#     m1=0
#     m2=1000000
#     mymin=0
#     mymax=0
#     dead=m2*0.9
#     n=0
#     mystr=''
#     while dead>a:
#         dead=random.randint(m1,m2)
#         if mymin>dead:
#             mymin=dead
#         elif mymax<dead:
#             mymax=dead
#         n=n+1
#     else:
#         mystr='{:4d} {:5d}   min:{:2d}   max: {:6d}   value: {:6d} '.format(a,n,mymin,mymax,dead)
#         print(mystr)
#         w(mystr)

#     #print('{:10d}'.format(n),'min','{:10d}'.format(mymin),'max','{:10d}'.format(mymax),'value','{:10d}'.format(dead))
#     return n

# for i in [1000,500,100,50,20,10,5,1]:

#     w('--'*20)
#     w('i = ',i)
#     f2.write(str(i))
#     f2.write(' : ')
#     #input('')
#     f2.write(str(test(i)))
#     f2.write('\n')
# f.close()
# f2.close()

def f3(m=1,n=1000000):
    '''返回小于m的数第一次出现在[0，n]区间的序号'''
    i=0
    x=n
    print('start......')
    while x>m:
        x=random.randint(0,n)
        i=i+1
    print('i =','{:5d}'.format(i))
    w('i =','{:5d}'.format(i))
    return i

print('a')

def mediannum(num):
    listnum = [num[i] for i in range(len(num))]
    listnum.sort()
    lnum = len(num)
    if lnum % 2 == 1:
        i = int((lnum + 1) / 2)-1
        return listnum[i]
    else:
        i = int(lnum / 2)-1
        return (listnum[i] + listnum[i + 1]) / 2



l=[]

for i in range(10000):
    print('第 {} 次'.format(i))
    l.append(f3())
print(l)

print('平均可得：{:,} 元'.format(sum(l)/len(l)))
print('中数可得：{:,} 元'.format(mediannum(l)))
print('最少可得：{:,} 元'.format(min(l)))
print('最多可得：{:,} 元'.format(max(l)))

w(l)
w('平均可得：{:,} 元'.format(sum(l)/len(l)))
w('中数可得：{:,} 元'.format(mediannum(l)))
w('最少可得：{:,} 元'.format(min(l)))
w('最多可得：{:,} 元'.format(max(l)))
f.close()