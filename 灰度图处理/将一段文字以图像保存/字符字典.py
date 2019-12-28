数字='0123456789'
英文字母='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
其他数字=''
特殊字符='~!@#$%^&*()_+{ }|:"[]……;<>?,./*-，。！·？'

def getid(字符:str):
    ''' 有一个字符获得1个数字,超出范围返回 999999'''
    try:
        v= ord(字符)
    except :
        v=999999
    return v

def getchar(id:int):
    ''' 有一个数字获得1个字符,超出范围返回 〇'''
    v=''
    try:
        v= chr(id)
    except :
        v='〇'
    return v