'''寻路算法学习'''
'''广度优先算法  所有地形通过速度一样
1.设定搜索起点S，放入openList中；判断openList是否为空，若为空，搜索结束；若不为空，拿出openList中的第一个节点G；
2.遍历G的上下左右四个相邻节点N1-N4，对每个节点N，如果N不在openList或closeList中，那么令N的父节点为G，将N放入openList中；
如果N已经在openList或closeList中，跳过不处理；
3.将G放入closeList中，重复步骤2.
'''


class P():
    def __init__(self, _x: int, _y: int):
        self.x = _x
        self.y = _y
        self.step = 0
        self.father = None
        self.id = '%d,%d' % (self.x, self.y)

    def find_in_list(self, *_list: list):
        for j in _list:
            for i in j:
                if i.id == self.id:
                    return True
        return False

    def display(self):
        pass  # print('this is  ', self.id, self.in_area)

    def check_in_area(self, _w, _h):
        self.in_area = True
        '''检查坐标是否在范围内'''
        if self.x < 0 or self.y < 0 or self.x > _w-1 or self.y > _h-1:
            #print('不在范围内', self.id)
            self.in_area = False
            return False
        return True


class Way():
    def __init__(self, _w=30, _h=20) -> None:
        self.h = _h
        '''最大行数'''
        self.w = _w
        '''最大列数'''
        self.start: P = P(0, 0)
        self.end: P = P(20, 20)
        self.unreachable = []
        #########
        self.l = [[' ' for i in range(self.w)] for j in range(self.h)]

    def set_unreachable(self):
        for i in self.unreachable:
            self.l[i.y][i.x] = i.step

    def findway(self):
        self.search = [self.start]          # 正在计算的点列表
        self.already = []  # 已搜索的点
        self._temp = []  # 中间过程值,即将搜寻的位置
        #############################################################
        while self.search != []:
            for i in self.search:
                for neibor in [P(i.x - 1, i.y), P(i.x + 1, i.y), P(i.x, i.y - 1), P(i.x, i.y + 1)]:
                    if not neibor.check_in_area(self.w, self.h):
                        continue
                    neibor.display()
                    if not neibor.find_in_list(self.search, self.already, self._temp, self.unreachable):
                        neibor.father = i
                        neibor.step = i.step+1
                        try:
                            self.l[neibor.y][neibor.x] = neibor.step
                        except:
                            input('error '+neibor.id)
                        self._temp.append(neibor)
            self.already = self.already+self.search
            if self.end.find_in_list(self.already):
                return
            self.search = self._temp
            self._temp = []


def printl(_l):
    '''测试用'''
    for i in _l:
        for j in i:
            print('{:3s}'.format(str(j)), end='')
        print('  ')

#######################################
# 测试用
w = Way(35, 20)
w.start = P(5, 5)
w.end = P(25, 10)
for i in range(18):
    w.unreachable.append(P(7, 19-i))
    w.unreachable.append(P(9, i))
    w.unreachable.append(P(11, 19-i))
for i in w.unreachable:
    i.step = '|'
for i in range(16):
    p = P(11+i, 16)
    p.step='———'
    w.unreachable.append(p)

w.set_unreachable()
w.findway()


for i in w.already:
    if i.id==w.end.id:
        rv=i
print(rv.id,rv.step)
while rv!=None:
    print(rv.id,rv.step)
    rv=rv.father