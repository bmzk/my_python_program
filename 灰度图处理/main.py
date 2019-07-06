
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
    for x in range(x1,x2+1):
        #print(x,'行开始')
        for y in range(y1,y2+1):
            img[x][y]=h
    print('设置 (',x1,y1,') (',x2,y2,')',h,'结束')

setheight(0,0,1080,1080,100)
setheight(240,240,850,850,30)
for i in range(5):
    for j in range(5):
        setheight(290+i*110,290+j*110,360+i*110,360+j*110,100)
        
setheight(500,0,540,290,30)
setheight(0,500,290,550,30)
setheight(500,800,550,1080,30)
setheight(800,500,1080,550,30)

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
