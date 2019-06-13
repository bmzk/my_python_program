import copy
 
def 计算角度改正数( 角度列表,角度闭合差):
    '''计算角度改正数
    a:角度闭合差
    n:角度数量'''
    改正后角度=copy.deepcopy(角度列表)
    n = len(角度列表)
    a=角度闭合差
    改正数=[0]
    角度列表_秒=[]
    for  i in 改正后角度:
        角度列表_秒.append(i.s_total)
    名次  = 排名(角度列表_秒)
    #print('计算角度改正数函数:名次=',名次)
    for i in range(1,n+1):
        改正数.append(int(-a // n))
        if a<0:
            if 名次[i-1] < (-a % n):#两数相除,余数跟除数同号
                改正数[i]+=1
        elif  (-a)==0 :
            pass
        else:
            if n-名次[i-1] <= (-a % n):#两数相除,余数跟除数同好
                改正数[i]+=1
    #print('计算角度改正数函数:输入数=',anglelist)
    #print('计算角度改正数函数:改正数=',改正数)
    return 改正数

def 排名(列表):
    '''给出列表中的元素的排名'''
    排名列表=copy.deepcopy(列表)
    顺序列表=copy.deepcopy(列表)
    顺序列表.sort(reverse=True)
    名次 = []
    列表长度=len(排名列表)
    for i in range( 列表长度):
        名次.append(len(排名列表))
    #print('排名列表=',排名列表)
    #print('顺序列表=',顺序列表)
    for i in range(列表长度):
        名次[i]=顺序列表.index(排名列表[i])
        顺序列表[名次[i]]=-1
        #print('>>',i,名次[i] , 排名列表[i])
    return 名次

def 计算坐标增量(边长列表:list,坐标增量闭合差:int ):
    '''本函数用于计算闭合导线坐标增量 
    d: 导线边长列表,边长应为整数,通常可以以毫米为单位
    zl:坐标增量列表,元素为整数
    gzs:坐标增量改正数列表,返回值
    n:导线边数量,int
    d_total:导线边长之和,int
    zl_total:坐标增量之和,int
    gzs_total:坐标增量改正数之和,int
    pm:边长的排名,list
    '''
    d=copy.deepcopy(边长列表)
    gzs=[0]
    n=len(边长列表)
    d_total=0
    gzs_total=-坐标增量闭合差
    for i in range(1,n):
        d_total+=d[i].l

    #临时列表
    d_temp=[]
    for i in range(n-1):
        d_temp.append(d[i+1].l)
    pm=排名(d_temp)
    for i in range(1,n):
        gzs.append(int(gzs_total*d[i].l/d_total))
    #log("gzs =",gzs)
    for i in range(1,n):
        gzs_total-=gzs[i]
    for i in range(1,n):
        if pm[i-1]<abs(gzs_total):
            try:
                gzs[i]-=int(坐标增量闭合差/abs(坐标增量闭合差))
            except  ZeroDivisionError:
                pass
            except:
                print('求坐标增量改正数出现错误')
    #log('边长列表',d_temp)
    #log('坐标增量闭合差',坐标增量闭合差)
    #log("gzs",gzs)
    return gzs

def log(*str):
    print('改正数 >>>',str)
    print()

