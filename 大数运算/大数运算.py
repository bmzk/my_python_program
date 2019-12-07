'''大数运算'''

import random


def jia():
    pass


def jian():
    pass


def log(*str):
    # print(str)
    pass


class 标准数字(object):
    '''将输入的数字格式化，分为整数、指数2部分'''

    def __init__(self, zhengshu=[], e=0):
        self.zhengshu = zhengshu
        self.e = e

    def tostring(self):
        string = ''
        if self.zhengshu[0] == 0:
            self.zhengshu[0] = ''
        for i in self.zhengshu:
            string += str(i)
        return string + ' +e'+str(self.e)


class 数学运算(object):
    def __init__(self, a=标准数字(), b=标准数字()):
        self.a = a
        self.b = b
        self.c = 标准数字()
        log('a', self.a.zhengshu)
        log('b', self.b.zhengshu)

    def cheng(self):
        '''计算两个任意数相乘'''
        v = []
        for i in range(len(self.a.zhengshu)+len(self.b.zhengshu)):
            v.append(0)
        log('v 初值：', v)
        for j in range(len(self.b.zhengshu)):
            for h in range(len(self.a.zhengshu)):
                v[-j-1-h] += self.b.zhengshu[-j-1]*self.a.zhengshu[-h-1]
                # log('v',v)
        log('v 中值：', v)
        # log('--'*20)
        for i in range(1, len(v)):
            v[-i-1] += v[-i] // 10
            v[-i] = v[-i] % 10
        log('v 终值：', v)
        self.c.zhengshu = v
        print('函数计算结果是：', self.c.tostring())


def __check():
    '''检测是否正确'''
    c = 0
    sc = '0'
    a = random.randint(10, 1000*1000)
    b = random.randint(10, 1000*1000)
    print('第1个数是：', a)
    print('第2个数是：', b)
    c = a*b
    print('直接计算结果是：', c)

    s = 数学运算()
    sa = []
    for i in range(len(str(a))):
        sa.append(int(str(a)[i]))
    s.a.zhengshu = sa

    sb = []
    for i in range(len(str(b))):
        sb.append(int(str(b)[i]))
    s.b.zhengshu = sb

    s.cheng()

    # print(len(str(a)),'+',len(str(b)),'=',len(str(c)),'=?=',len(s.c.zhengshu))

    if str(c) == str(s.c.tostring().split()[0]):
        print('结果正确====================')
    else:
        print('====================结果错误')
    print('结果是', len(str(c)), '位数字')


if __name__ == '__main__':
    for i in range(9):
        print('>>'*2, i, '--'*10)
        __check()
