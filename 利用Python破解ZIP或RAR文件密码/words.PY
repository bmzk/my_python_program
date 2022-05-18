#words=u'"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVEXYZ!@#$%^&*(){-=+},./?\\。，'

from numpy import int256


words=u' "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVEXYZ!@-=+},./?\\。，'



class ds():
    def __init__(self,LENGTH:int=20,start=0) -> None:
        self.k=[0]
        self.set_n(start)

    def gain(self,n=0):
        self.k[n]=self.k[n]+1
        if self.k[n]>len(words)-1:
            if len(self.k)<n+2:
                self.k.append(0)
            else:
                self.gain(n+1)

    def get_s(self):
        rv=[]
        for i in self.k:
            rv=words[i]+rv
        ds.gain(0)

    def set_n(self,n):
        self.k=[]
        for i in range(n):
            self.gain(0)




d=ds(8999)
for i in range(8999,9999):
    s=ds.get_s()


