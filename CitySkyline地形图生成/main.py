'''用于游戏 城市：天际线（City:Skyline）生成地形图'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

plt.figure("beautifulscene")
file = 'img源文件.png'
img = mpimg.imread(file)


# 读取照片，照片都是一堆像素

# r,g,b = [img[:,:,i] for i in range(3)]
# img_gray = r*0.299+g*0.587+b*0.114


def setheight(x1, y1, x2, y2, h):
    '''设置 (x1,y1) (x2,y2)区域高程为h'''
    for x in range(x1, x2 + 1):
        # print(x,'行开始')
        for y in range(y1, y2 + 1):
            img[x][y] = h/1024
    print('设置 (', x1, y1, ') (', x2, y2, ')', h, '结束')


##########################################################
### 设定基础值，本部分内容无需修改 #########################
print('程序开始')
# 设置边框为0
setheight(0, 0, 1080, 1080, 0)
setheight(20, 20, 1071, 1071, 50)
# 设定最高值，用于调整地形，进入游戏后需手动抹平
setheight(0, 0, 10, 10, 1023)
###########################################################
### 自定义区域，需要修改 ###################################
setheight(530, 0, 550, 1080, 30)
setheight(0, 530, 1080, 550, 30)
##########################################################
### 程序结尾，不需修改 ####################################
# 将像素转换为单通道照片，照片一般是3通道的rgb模式
plt.imshow(img, cmap="gray")
plt.show()
outFile = 'image-out.png'
mpimg.imsave(outFile, img, cmap="gray")
print('end')
