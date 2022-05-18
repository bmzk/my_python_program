# -*- coding:utf-8 -*-
from turtle import TurtleScreen
import zipfile #导入模块，它是做压缩和解压缩的
import os
import time
import words
##########################
myfile='D:\\BaiduNetdiskDownload\\tianxin2-160G\\tianxin2.zip'
zfile = zipfile.ZipFile(myfile)

t0= time.time()
filename='zip-password-crack'+time.strftime('%H:%M:%S',time.localtime())+'.txt'



def w(pwd,t='',id=0):
    f=open(filename,'a',encoding='utf-8')
    f.write(id+'    '+t+'    '+pwd)
    f.close()

def zipcrack(password:str):
    # time.sleep(0.5)
    t = time.time()
    password=password.replace(' ','')
    s=str(words.k)+time.strftime('    %H:%M:%S',time.localtime(time.time()-t0))+'    密码是：'+password +'    ' + filename
    try:
        print(s)
        w(s)
        zfile.extractall(path=os.getcwd(), pwd=password.encode('utf-8'))
        #break
        input('密码正确 '+password)
        quit()
    except Exception as e:
        #print(e)
        pass

words.set_n( int(input('输入起始数：')))
while True:
    zipcrack(words.get_s())

