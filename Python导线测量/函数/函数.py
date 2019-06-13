import time
import 函数.类定义

def log(*mystr,width=20,l_c_r='c'):
    v=''
    for i in mystr:
        if l_c_r=="l":
            v+=str(i).ljust(width)
        elif l_c_r=="r":
            v+=str(i).rjust(width)
        else:
            v+=str(i).center(width)
    print(v)
    print()

