def f(x,n):
    '''泰勒级数的多项式'''
    rv=x

import math
print(math.cos(0.1))
k=1
for i in range(30):
    k=k/(i+1)
    print(str(i).rjust(2),str(k).ljust(25),str(math.cos(k)).ljust(20))
    input("输入任意值继续。。。")