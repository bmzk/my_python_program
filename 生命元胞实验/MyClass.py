'''
类定义文件
用于定义类
'''
import random
import wx
import var

'''

'''

cellList=[]
cellCount=var.row * var.column
class cell(object):
    '''一个单元格的类'''
    def __init__(self, panel,id,_size=25):
        '''  
        '''
        # 创建一个标签,坐标(n,0)
        self.level  = 0
        self.id     = id
        self.x      = id // var.column # 所在的行号
        self.y      = id % var.column   # 所在的列号
        self.cells  = self.获取某格周围的单元格(self.x,self.y) # 相邻的行,列
        self.box    = 0#,style=wx.Centre)
        #self.box.SetBackgroundColour('#888888')

    def refresh(self):
        '''
        '''
        # 设置单元格状态
        self.box.SetLabel(str(self.level))
        _colour = '#'+'{:0>2x}'.format(80*self.level)+'{:0>2x}'.format(255-80*self.level)+'00'
        self.box.SetBackgroundColour(_colour)

    def 计算元胞获取的能量(self):
        rv=0
        for i in self.cells['rows']:
            for j in self.cells['columns']:
                rv=rv+self.计算从某格获取的能量(i,j)
        return rv

    def 计算从某格获取的能量(self,x,y):
        '''从一个单元格中获取的能量'''
        return var.power * self.level / self.计算某格周围总元胞等级(x,y)

    def 计算某格周围总元胞等级(self, x, y):
        cells = self.获取某格周围的单元格( x, y)
        rv=0
        for i in  cells['rows'] :
            for j in cells['columns'] :
                rv=rv+self.获取某格元胞等级(i,j)
        if rv == 0 :
            rv = 1
        return rv

    def 获取某格元胞等级(self,x,y):
        return cellList[x * var.column + y].level

    def 元胞成长(self):
        if self.计算元胞获取的能量() < var.dieEnergy:
            self.level=0
            return 0
        elif self.level > 0 :
            self.level = self.level + 1
            if self.level > var.maxAge :
                self.level = 0#var.maxAge 

    def 元胞繁殖(self):
        if self.level < var.bornAge :
            return 0  # 跳出函数
        空位=[]
        for i in self.cells['rows']:
            for j in self.cells['columns']:
                if self.获取某格元胞等级(i,j) == 0 :
                    空位.append(i * var.column + j)
        if len(空位) > 0:
            _p = 空位[random.randint(0,len(空位)-1)]
            cellList[_p].level = 1




    def 获取某格周围的单元格(self, x, y):
        '''x:所在行 \n y:所在列'''
        rows   = []    # 相邻的行
        columns= []    # 相邻的列
        if x == 0 :
            rows = [0,1]
        elif x == var.row-1 :
            rows = [x-1 , x ]
        else:
            rows = [x-1 ,x,x+1]

        if y == 0 :
            columns = [0,1]
        elif y ==  var.column - 1 :
            columns = [y-1, y]
        else :
            columns = [y-1, y, y+1]

        return {'rows':rows, 'columns':columns}



