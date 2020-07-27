import sys
import time
import os
#f=sys.argv[1]
f=''
print(f)
原文件夹路径=r'C:\Users\asd\Desktop\f1'

文件夹名称 = 原文件夹路径.split('\\')[-1]
#[-1]
print('要备份的文件夹是:',文件夹名称)
print('请输入备份的 备注 :')
备注 = '手动备份'#input('备注:   ')

备份名称=time.strftime('%Y_%m_%d-%H_%M_%S--',time.localtime())+备注
print('备份名称为:',备份名称)
备份路径='C:\\Users\\asd\\Desktop\\bak\\'
目标文件夹路径 = 备份路径 + 文件夹名称 + '\\'+备份名称 +'\\'

print('原文件夹',原文件夹路径)
print('目标文件夹',目标文件夹路径)
os.system(r'c:\windows\system32\xcopy %s %s /E/y' % (原文件夹路径, 目标文件夹路径))


for i in range(5):
    print(5-i,'秒后本窗口将自动关闭...')
    time.sleep(1)







#os.system('shutdown -s -t 1')