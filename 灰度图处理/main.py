
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg
import numpy as np
 
plt.figure("beautifulscene")
file='C:\\Users\\bmzk1\\Documents\\GitHub\\my_python_program\\灰度图处理\\image35.png'
img = mpimg.imread(file)   
#读取照片，照片都是一堆像素  

# r,g,b = [img[:,:,i] for i in range(3)]
# img_gray = r*0.299+g*0.587+b*0.114


def setheight(x1,y1,x2,y2,h):
    '''设置 (x1,y1) (x2,y2)区域高程为h'''
    for x in range(x1,x2+1):
        #print(x,'行开始')
        for y in range(y1,y2+1):
            img[x][y]=h
    print('设置 (',x1,y1,') (',x2,y2,')',h,'结束')




def createarea(_s=250 ,_d=80):
    '''绘制5X5城市区域  \n
    #绘图区域起点x坐标（y坐标等于x作弊中） _s=250 \n
    #地块宽度 _d=80 \n
    '''
    # 海平面高程为40.设置基本高程
    h=45
    hd=35#地面高程
    setheight(0,0,1080,1080,h)
    setheight(250,250,830,830,hd)
    #间隔（水域宽度）
    jg=round((1080-2*_s-5*_d)/6)
    print('间隔（水域宽度）: ',jg)
    _ss=(_s+jg)
    w=(_d+jg)
    for i in range(5):
        for j in range(5):
            setheight(_ss + w * i , _ss + w * j ,
                (_ss+_d)+w*i,(_ss+_d)+w*j,h)
    pass
    setheight(530,0,550,260,hd)
    #setheight(0,530,260,550,30)
    #setheight(530,820,550,1080,30)
    #setheight(820,530,1080,550,30)


createarea()

#设定最高和最小高程，无需改动
setheight(0,0,100,100,1024)
setheight(100,100,200,200,0)
plt.imshow(img,cmap="gray")  
#plt.imshow(img_gray,cmap="gray")  
#plt.imshow(img) 
#将像素转换为单通道照片，照片一般是3通道的rgb模式
plt.show()
file2='C:\\Users\\bmzk1\\Documents\\GitHub\\my_python_program\\灰度图处理\\image-out.png'
mpimg.imsave(file2,img,cmap="gray")
#plt.savefig(file2)
print('end')
