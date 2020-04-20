class unit(object):
    def __init__(self,txt):
        self.momeny=1000
        self.count=100
        self.txt=txt
        self._=0
    def product(self,obj):
        if self.momeny< obj.count :
            self._=self.momeny
        else:
            self._=obj.count
        self._=int(obj.count*0.5)
        self.count=self.count+self._*2
        self.momeny=self.momeny-self._
        obj.count=obj.count-self._
        obj.momeny=obj.momeny+self._
        print(self.txt,f(self.momeny),(self.count))

def f(n):
    '''格式化数字'''
    return "{:8d}".format(n)


day=1
momeny=0
A=unit("A")
B=unit("B")
C=unit("C")

def day_sub():
    global day
    print("day",day)
    day=day+1
    A.product(C)
    print("momeny:",f(A.momeny),f(B.momeny),f(C.momeny),f(A.momeny+B.momeny+C.momeny))
    print(" count:",f(A.count),f(B.count),f(C.count),f(A.count+B.count+C.count))
    B.product(A)
    print("momeny:",f(A.momeny),f(B.momeny),f(C.momeny),f(A.momeny+B.momeny+C.momeny))
    print(" count:",f(A.count),f(B.count),f(C.count),f(A.count+B.count+C.count))
    C.product(B)
    print("momeny:",f(A.momeny),f(B.momeny),f(C.momeny),f(A.momeny+B.momeny+C.momeny))
    print(" count:",f(A.count),f(B.count),f(C.count),f(A.count+B.count+C.count))

a=""
while a !="no":
    import os
    os.system("cls") 
    day_sub()
    str=input("是否继续(默认yes) yes/no")
    if str=="g":
        A.momeny=A.momeny+1000
    print("-"*20)
