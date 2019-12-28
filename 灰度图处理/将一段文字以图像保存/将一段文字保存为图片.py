'''将一段文字保存为图片'''

import matplotlib.image as mpimg
import random
import GetTime
import numpy
import 字符字典
file = 'C:\\Users\\asd\\Documents\\GitHub\\my_python_program\\灰度图处理\\image.png'
img = mpimg.imread(file)
# 读取照片，照片都是一堆像素

def __chartoint(mychar,k=50):
        '''给出一个字符返回1个整数列表[r,g,b,1]'''
        rgb = 字符字典.getid(mychar)
        r = rgb//(k*k)/k
        g = (rgb//k) % k/k
        b = rgb % k/k
        return [r, g, b,1.0]# random.random()]
def str_to_arr(输入字符串,tw=(5,5) ):
    '''给出一个字符串返回1个浮点数列表
    tw : 图斑宽度和高度'''
    import math    ##########################################
    w = int(math.sqrt(len(输入字符串)))+1 #图片宽度，图片的宽和高相等
    imgarr = []
    #
    b1=int(w*tw[0]*w*tw[1]/100)+1
    for i in range(w*tw[0]):
        imgarr.append([])
        for j in range(w*tw[1]):
            x=i//tw[0]
            y=j//tw[1]
            id=x*w+y
            if id<len(输入字符串):
                imgarr[i].append( __chartoint(输入字符串[id]))
            else :
                imgarr[i].append([1.0,1.0,1.0, 1.0])
            #
            if (i*w*tw[1]+j) % b1 ==0:
                print('计算图形数据：',"{:2d}".format((i*w*tw[1]+j) // b1),'%')

    print( '计算图形数据完成','####'*20)
    #print(type(ia))
    ia = numpy.array(imgarr)#, dtype=numpy.uint8)
    return ia


def saveimg(fname, 图片数组):
    '''将图形数据以PNG图片格式保存在电脑上。'''
    #print(len(图片数组), type(图片数组))
    #print(图片数组)
    mpimg.imsave(fname, 图片数组)


def main(fname):
    '''主程序'''
    print('提示：如果直接回车，要转换的文字将为“要转换的文字.txt”中的文字')
    ms=input('输入要转换成图片的文字: \n ')
    print('开始时间：',GetTime.getTime())
    if ms=='':
        try:
            f=open('要转换的文字.txt','r',encoding='utf-8')
            ms=str(f.readlines())
            f.close()
        except :
            print('缺少默认文件')
    print('len(ms)=',len(ms))
    print('start', GetTime.getTime())
    saveimg(fname,str_to_arr(ms))
    print('结束时间：',GetTime.getTime())
    input('按任意键继续')



if __name__ == '__main__':
    #for i in range(9):
    filename = GetTime.getTime(2)+'.png'
    main(filename)
    print(filename,'is ok')
    print('end', '--'*10)

