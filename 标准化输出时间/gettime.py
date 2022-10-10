'''标准化输出时间
时间日期格式化符号：
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%M 分钟数（00=59）
%S 秒（00-59）
%W 一年中的星期数（00-53）星期一为星期的开始
'''
import time

def gt(type=0):
    '''dfgfg
    '''
    rv=0
    if type==0:
        return time.strftime('%Y',time.localtime())



def st(f='%Y%m'):
    return time.strftime('%Y%m%d-%H%M%S',time.localtime())

