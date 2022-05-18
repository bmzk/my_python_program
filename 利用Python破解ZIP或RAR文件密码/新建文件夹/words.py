words = u' 0123456789abcdefghijklmnopqrstuvwxyz.'


k=[1,0,0,0,0]
def __init__( start=0):
    global k
    k =[1,0,0,0,0]
    set_n(start)
    print('init',self)

def gain( n=0):
    global k
    k[n] = k[n]+1
    if k[n] > len(words)-1:
        k[n]=0
        if len(k) < n+2:
            k.append(0)
        gain(n+1)

            # print('asdasdas')

def get_s():
    rv = ''
    gain()
    for i in k:
        try:
            rv = words[i]+rv
        except:
            print('i=',i)
            quit()
    return rv

def set_n( n):
    global k
    k = [1,0,0,0,0]
    for i in range(n):
        gain(0)



# for i in range(8999,9999):
print('d=',len(words))
#s = get_s()
print('import words 结束 =================')

