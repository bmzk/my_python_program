# -*- coding:utf-8 -*-
from turtle import TurtleScreen
import zipfile #导入模块，它是做压缩和解压缩的
import os
import time

##########################
myfile='D:\\BaiduNetdiskDownload\\tianxin2-160G\\tianxin2.zip'
zfile = zipfile.ZipFile(myfile) #要解压缩的压缩包

print(zfile.infolist)






